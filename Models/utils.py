import os
import random
from PIL import Image

def load_random_image_from_folder(folder_path):
    """Returns a random image from a given folder as a PIL image."""
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if not images:
        raise FileNotFoundError("No image files found in the folder.")
    img_path = os.path.join(folder_path, random.choice(images))
    return Image.open(img_path)

def clean_label(label: str) -> str:
    """Normalize label string for comparison."""
    return label.strip().lower().replace(" ", "")
