import os
import torch
import torchvision.transforms as transforms
from torch import nn
from PIL import Image
import pickle
from pathlib import Path
from tqdm import tqdm
from torch.utils.data import DataLoader, Dataset
import numpy as np
from torchvision.models import resnet34
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import uuid
import sys

# Unique script execution ID for debugging
SCRIPT_ID = str(uuid.uuid4())

def main():
    print(f"Starting feature_extractor.py with ID: {SCRIPT_ID}")

    # Paths
    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = BASE_DIR / "processed_data"
    OUTPUT_DIR = BASE_DIR / "extracted_features"
    MODEL_DIR = BASE_DIR / "trained_models"

    # Delete old features directory
    if OUTPUT_DIR.exists():
        print("⚠️ Deleting old extracted_features...")
        import shutil
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # ResNet-34 for feature extraction
    class ResNetFeatureExtractor(nn.Module):
        def __init__(self):
            super(ResNetFeatureExtractor, self).__init__()
            self.resnet = resnet34()
            # Try to load fine-tuned weights
            weights_path = MODEL_DIR / "best_model_resnet34_end_to_end.pth"
            if weights_path.exists():
                print(f"Loading fine-tuned ResNet-34 weights from {weights_path}")
                state_dict = torch.load(weights_path, map_location=device)
                self.resnet.load_state_dict(state_dict, strict=False)
            else:
                print("Fine-tuned weights not found, using pre-trained ImageNet weights")
                self.resnet = resnet34(weights="IMAGENET1K_V1")
            self.resnet.fc = nn.Identity()  # Remove final FC layer

        def forward(self, x):
            return self.resnet(x)

    # Image transformations
    train_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(20),
        transforms.RandomResizedCrop(224, scale=(0.8, 1.0)),
        transforms.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.4),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    val_test_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    # Custom Dataset for loading images
    class ImageDataset(Dataset):
        def __init__(self, split_folder, transform):
            self.split_folder = split_folder
            self.transform = transform
            self.img_paths = []
            self.labels = []

            for person in os.listdir(split_folder):
                person_folder = split_folder / person
                if person_folder.is_dir():
                    images = [person_folder / img_name for img_name in os.listdir(person_folder)]
                    if len(images) < 20:
                        print(f"Warning: {person} has only {len(images)} images in {split_folder.name}")
                    for img_path in images:
                        self.img_paths.append(img_path)
                        self.labels.append(person)

        def __len__(self):
            return len(self.img_paths)

        def __getitem__(self, idx):
            img_path = self.img_paths[idx]
            label = self.labels[idx]
            img = Image.open(img_path).convert("RGB")
            img = self.transform(img)
            return img, label

    # Function to extract features in batches
    def extract_features_batch(dataloader, model):
        all_features = []
        all_labels = []
        with torch.no_grad():
            for imgs, labels in tqdm(dataloader, desc="Extracting features"):
                imgs = imgs.to(device)
                features = model(imgs)
                all_features.append(features.cpu().numpy())
                all_labels.extend(labels)
        
        return np.concatenate(all_features, axis=0), all_labels

    # Function to visualize features using t-SNE
    def visualize_features(features, labels, output_path):
        tsne = TSNE(n_components=2, random_state=42)
        features_2d = tsne.fit_transform(features)
        unique_labels = sorted(set(labels))
        plt.figure(figsize=(12, 10))
        for label in unique_labels[:20]:  # Limit to 20 classes for clarity
            idx = [i for i, l in enumerate(labels) if l == label]
            plt.scatter(features_2d[idx, 0], features_2d[idx, 1], label=label, alpha=0.5)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.savefig(output_path, bbox_inches='tight')
        plt.close()

    # Main loop
    print(f"Entering main() with SCRIPT_ID: {SCRIPT_ID}")
    splits = ['train', 'val', 'test']
    model = ResNetFeatureExtractor().to(device)
    model.eval()
    all_features = {}
    
    for split in splits:
        transform = train_transform if split == 'train' else val_test_transform
        split_folder = DATA_DIR / split
        print(f"Processing {split} set...")

        # Create Dataset and DataLoader
        dataset = ImageDataset(split_folder, transform)
        dataloader = DataLoader(dataset, batch_size=32, shuffle=False, num_workers=0)

        # Extract features
        features, labels = extract_features_batch(dataloader, model)
        all_features[split] = {
            "features": features,
            "labels": labels
        }

        # Visualize features for train set
        if split == 'train':
            visualize_features(features, labels, OUTPUT_DIR / "tsne_resnet34.png")

    # Save extracted features
    with open(OUTPUT_DIR / "features_resnet34.pkl", "wb") as f:
        pickle.dump(all_features, f)
    print(f"✅ Features saved at extracted_features/features_resnet34.pkl")

if __name__ == "__main__":
    main()