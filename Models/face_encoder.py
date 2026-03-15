import os
import face_recognition
import pickle
from tqdm import tqdm
from pathlib import Path
from PIL import Image

# Define paths
BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "data" / "Celebrity_images"
EMBEDDINGS_PATH = BASE_DIR / "data" / "embeddings.pkl"

# Store embeddings and labels
embeddings = []
labels = []

# Loop over each celebrity folder
for celeb_name in os.listdir(DATASET_DIR):
    celeb_folder = DATASET_DIR / celeb_name
    if not celeb_folder.is_dir():
        continue

    print(f"\nProcessing {celeb_name}...")


    

    for img_name in tqdm(os.listdir(celeb_folder)):
        img_path = celeb_folder / img_name

        # Load image using face_recognition
        try:
            image = face_recognition.load_image_file(img_path)
            face_locations = face_recognition.face_locations(image)

            if len(face_locations) != 1:
                print(f"Skipping {img_name}: Found {len(face_locations)} faces")
                continue

            # Encode the face (128-d vector)
            face_encoding = face_recognition.face_encodings(image, known_face_locations=face_locations)[0]
            embeddings.append(face_encoding)
            labels.append(celeb_name)

        except Exception as e:
            print(f"Error processing {img_name}: {e}")

# Save embeddings and labels using pickle
with open(EMBEDDINGS_PATH, "wb") as f:
    pickle.dump({"embeddings": embeddings, "labels": labels}, f)

print(f"\n✅ Encoding complete! Saved {len(embeddings)} embeddings to {EMBEDDINGS_PATH}")
