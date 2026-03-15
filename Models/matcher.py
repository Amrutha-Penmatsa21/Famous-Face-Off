import face_recognition
import pickle
from pathlib import Path
from scipy.spatial.distance import cosine
from PIL import Image
import random
import os
import tkinter as tk
from tkinter import messagebox

# Load the embeddings and labels
BASE_DIR = Path(__file__).resolve().parent
EMBEDDINGS_PATH = BASE_DIR / "data" / "embeddings.pkl"

with open(EMBEDDINGS_PATH, "rb") as f:
    data = pickle.load(f)

known_embeddings = data["embeddings"]
known_labels = data["labels"]

# Load input image
INPUT_IMAGE_PATH = BASE_DIR / "data" / "aswini6.jpg"
input_image = face_recognition.load_image_file(INPUT_IMAGE_PATH)
input_encodings = face_recognition.face_encodings(input_image)

if not input_encodings:
    print("❌ No face found in the input image.")
    exit()

input_encoding = input_encodings[0]

# Find best match using cosine similarity
def find_best_match(input_encoding, known_embeddings, known_labels):
    distances = [cosine(input_encoding, emb) for emb in known_embeddings]
    best_match_idx = distances.index(min(distances))
    return known_labels[best_match_idx], min(distances)

best_match, similarity = find_best_match(input_encoding, known_embeddings, known_labels)

# Calculate match percentage
match_percentage = (1 - similarity) * 100

# Terminal output
print(f"🎯 Best Match: {best_match}")
print(f"🧠 Cosine Similarity Score: {1 - similarity:.4f}")
print(f"📊 Match Percentage: {match_percentage:.2f}%")

# Display matched celebrity image
celeb_folder = BASE_DIR / "data" / "Celebrity_images" / best_match
sample_image = random.choice(os.listdir(celeb_folder))
sample_image_path = celeb_folder / sample_image
img = Image.open(sample_image_path)
img.show()

# Optional popup message
root = tk.Tk()
root.withdraw()
messagebox.showinfo(
    "Match Found",
    f"🎯 {best_match}\n🧠 Cosine Similarity: {1 - similarity:.4f}\n📊 Match Score: {match_percentage:.2f}%"
)
