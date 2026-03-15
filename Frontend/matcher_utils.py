# matcher_utils.py
import face_recognition
import pickle
from pathlib import Path
from scipy.spatial.distance import cosine
from PIL import Image
import os
import random

BASE_DIR = Path(__file__).resolve().parent.parent # Moves up to Famousfaceoff1/
EMBEDDINGS_PATH = BASE_DIR / "Models" / "data" / "embeddings.pkl"

print(f"Looking for embeddings at: {EMBEDDINGS_PATH}")
if not os.path.exists(EMBEDDINGS_PATH):
    raise FileNotFoundError(f"Embeddings file does not exist at: {EMBEDDINGS_PATH}")

try:
    with open(EMBEDDINGS_PATH, "rb") as f:
        data = pickle.load(f)
except Exception as e:
    raise Exception(f"Failed to load embeddings.pkl: {e}")

known_embeddings = data["embeddings"]
known_labels = data["labels"]

def find_best_match(image_path):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    
    if not encodings:
        return None, None, None
    
    input_encoding = encodings[0]
    distances = [cosine(input_encoding, emb) for emb in known_embeddings]
    best_match_idx = distances.index(min(distances))
    best_label = known_labels[best_match_idx]
    similarity = 1 - distances[best_match_idx]

    celeb_folder = BASE_DIR / "Models" / "data" / "Celebrity_images" / best_label
    celeb_image = random.choice(os.listdir(celeb_folder))
    celeb_image_path = celeb_folder / celeb_image

    return best_label, similarity, str(celeb_image_path)