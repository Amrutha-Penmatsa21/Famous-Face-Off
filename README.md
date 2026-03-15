# 🎬 CLARA – Celebrity Look-Alike Recognition Application

## Famous Face-Off: Celebrities and Their Surprising Look-Alikes

Discover which Indian celebrity you look like! **CLARA** (Celebrity Look-Alike Recognition Application) is an intelligent facial recognition desktop application that matches user photos with Indian celebrities and finds surprising lookalikes. Using advanced deep learning techniques, the application analyzes facial features and provides similarity scores with **complete offline capability** and **zero external dependencies**.

---

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Results](#results)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## 🎯 Overview

**CLARA** (Celebrity Look-Alike Recognition Application) is a **standalone Python-based desktop application** that uses advanced facial recognition and deep learning to match user images with Indian celebrities. Unlike cloud-based solutions, CLARA works **completely offline**, ensuring **100% privacy and data security**.

### Key Highlights:
- **Standalone Desktop App** - No web server, no cloud dependency, no internet required
- **Real-time webcam matching** - Capture your face directly from webcam
- **Image file upload** - Upload custom images for analysis
- **High-accuracy matching** - Uses 128D face embeddings and cosine similarity
- **Beautiful GUI** - Modern PyQt5-based interface with smooth animations
- **Large celebrity database** - **110+ Indian celebrities** with 50+ images each (5000+ total images)
- **Result Management** - Save, Share, and Delete matched results
- **Built-in Manual** - User guidance for first-time users
- **Privacy-First** - Fully local processing, no external APIs or servers

---

## ✨ Features

### Core Features
✅ **Face Detection & Encoding** - Automatically detects and encodes faces using face_recognition library (128D embeddings)
✅ **Similarity Matching** - Compares input face with 110+ Indian celebrities using cosine similarity & Euclidean distance
✅ **Real-time Webcam** - Live video feed with instant face detection and matching
✅ **Image Upload** - Upload custom images for analysis and matching
✅ **Match Percentage** - Shows confidence score (0-100%) for matches with detailed similarity metrics
✅ **Error Handling** - Gracefully handles cases where no face is detected in uploaded images
✅ **Celebrity Database** - **110+ Indian celebrities** with 50+ images each (5000+ total):
   - **Bollywood** - Shah Rukh Khan, Priyanka Chopra, Deepika Padukone, Katrina Kaif, Ranbir Kapoor, etc.
   - **Sports** - Virat Kohli, MS Dhoni, Sachin Tendulkar, Hardik Pandya, Jasprit Bumrah, etc.
   - **Tollywood** - Prabhas, Mahesh Babu, Ram Charan, Jr NTR, Allu Arjun, etc.
   - **Tamil Cinema** - Rajinikanth, Surya, Dhanush, Tamannaah, Nithya Menon, etc.
   - **Music Artists** - Arijit Singh, Shreya Ghoshal, Jubin Nautiyal, Palak Muchhal, etc.
   - **Other Celebrities** - Politicians, Regional stars, and more

### GUI Features
🎨 **Interactive PyQt5 Interface** - Modern, responsive desktop application with gradient backgrounds
🎨 **Splash Screen** - Professional branded splash screen with animations
🎨 **Smooth Transitions** - Animated page transitions using QPropertyAnimation and QEasingCurve
🎨 **Drop Shadow Effects** - Professional UI styling with depth and visual hierarchy
🎨 **Real-time Preview** - Live webcam feed with face detection overlay
🎨 **Result Management** - Save, Share, and Delete matched results
🎨 **Built-in Manual** - Comprehensive user guide for first-time users

### Privacy & Security
🔐 **100% Offline** - Works completely offline, no internet connection required
🔐 **No Cloud Dependency** - No external APIs, no data sent anywhere
🔐 **Local Processing** - All face encoding and matching happens on your machine
🔐 **Data Privacy** - Your images never leave your computer  

---

## 🛠️ Technologies Used

### Backend & ML
- **Python 3.x** - Core programming language
- **face_recognition** - Deep learning facial recognition (dlib CNN model)
- **face_recognition_models** - Pre-trained face encoding models
- **dlib** - Face detection and alignment
- **scipy** - Cosine similarity distance calculations
- **Pillow (PIL)** - Image processing
- **OpenCV** - Video capture and image processing

### Deep Learning & Computer Vision
- **PyTorch** - Deep learning framework
- **torchvision** - Computer vision utilities (ResNet-34 for feature extraction)
- **ResNet-34 CNN** - Convolutional Neural Network for advanced feature extraction
- **NumPy** - Numerical computations
- **scikit-learn** - Machine learning utilities
- **scikit-image** - Image processing algorithms

### GUI Framework
- **PyQt5** - Desktop GUI application framework
- **PyQt5_sip** - SIP bindings for PyQt5

### Additional Libraries
- **NumPy** - Numerical operations
- **SciPy** - Scientific computing
- **tqdm** - Progress bars
- **SymPy** - Symbolic mathematics

---

## 📁 Project Structure

```
Famous-Face-Off/
│
├── Frontend/
│   ├── frontend.py                 # Main PyQt5 GUI application
│   ├── matcher_utils.py            # Face matching utilities
│   ├── requirements.txt            # Frontend dependencies
│   └── __pycache__/
│
├── Models/
│   ├── face_encoder.py             # Face encoding generation script
│   ├── feature_extractor.py        # Deep feature extraction (ResNet-34)
│   ├── matcher.py                  # Core matching algorithm
│   ├── utils.py                    # Utility functions
│   │
│   └── data/
│       ├── Celebrity_images/        # 100+ celebrity folders
│       │   ├── Aditya_roy_kapoor/
│       │   ├── Aishwarya_rai/
│       │   ├── Akshay_kumar/
│       │   ├── Shah_rukh_khan/
│       │   ├── MS_Dhoni/
│       │   ├── Sachin_Tendulkar/
│       │   └── ... (90+ more celebrities)
│       │
│       ├── embeddings.pkl          # Pre-computed face encodings
│       └── test_images/            # Test dataset
│
├── requirements.txt                 # Main project dependencies
├── README.md                        # This file
└── .gitignore
```

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager
- Webcam/Camera (for real-time feature)
- 2GB+ available storage (for celebrity database and models)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/Famous-Face-Off.git
cd Famous-Face-Off
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

**Activate Virtual Environment:**
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Install dlib (if face_recognition fails):**
```bash
pip install dlib
```

Or use pre-built wheels:
```bash
pip install dlib-bin
```

### Step 4: Generate Face Encodings (First Time Only)
```bash
cd Models
python face_encoder.py
```
This generates the `embeddings.pkl` file containing all celebrity face encodings.

---

## � Celebrity Dataset

### Accessing the Celebrity Database

The application requires a dataset of 110+ Indian celebrity images (5000+ total images) to function. Due to file size and licensing considerations, this dataset is **not included** in the GitHub repository.

### How to Get the Dataset

**To access the celebrity dataset, please contact us:**

📧 **Email:** [Check this file(https://github.com/Amrutha-Penmatsa21/Famous-Face-Off/blob/main/DATASET_REQUEST.md) ]  
📱 **GitHub:** Create an [Issue](https://github.com/yourusername/Famous-Face-Off/issues) with the subject "Dataset Request"

### After Receiving the Dataset

1. Extract the celebrity images to: `Models/data/Celebrity_images/`
2. The folder structure should be:
   ```
   Models/data/Celebrity_images/
   ├── Shah_rukh_khan/
   ├── Virat_Kohli/
   ├── Priyanka_Chopra/
   ├── Sachin_Tendulkar/
   └── ... (110+ celebrity folders)
   ```
3. Run the face encoder:
   ```bash
   cd Models
   python face_encoder.py
   ```
4. This will generate `embeddings.pkl` with all face encodings
5. Run the application:
   ```bash
   cd Frontend
   python frontend.py
   ```

### Why Separate Dataset?

- ✅ **Faster Repository Cloning** - Repository size stays small (~5MB instead of ~2GB)
- ✅ **File Size Management** - Keep GitHub repo optimized
- ✅ **Licensing Control** - Better management of celebrity image usage rights
- ✅ **Easy Updates** - Dataset can be updated without re-cloning

---

## �💻 Usage

### Run the Application

```bash
cd Frontend
python frontend.py
```

### Application Features

1. **Splash Screen** - Initial welcome screen with app branding
2. **Main Interface** - Choose between webcam or image upload
3. **Webcam Matching:**
   - Click "Capture from Webcam"
   - Allow camera access
   - Face will be automatically detected
   - Matching happens in real-time
4. **Image Upload:**
   - Click "Upload Image"
   - Select any image file from your system
   - App analyzes and matches the face
5. **Results Display:**
   - Shows matched celebrity name
   - Displays match percentage (confidence score)
   - Shows sample image of matched celebrity
   - Option to try again

---

## 🧠 How It Works

### 1. **Face Encoding** (Preprocessing)
The application generates **128-dimensional embeddings** for all faces in the dataset:
- Images are loaded using the `face_recognition` library
- Face detection happens using dlib's **deep learning CNN model**
- Each face is converted to a **128D vector** (face encoding) that uniquely represents facial features
- All 110+ celebrities with 50+ images each = 5000+ face encodings
- Encodings are pre-computed and stored in `embeddings.pkl` for fast lookup

```python
# Face encoding generation
import face_recognition
image = face_recognition.load_image_file("path/to/image.jpg")
face_locations = face_recognition.face_locations(image)  # Detect faces
face_encodings = face_recognition.face_encodings(image, face_locations)  # Generate 128D vectors
```

### 2. **Feature Extraction** (Advanced)
- Deep feature extraction using **ResNet-34 CNN** (PyTorch)
- ResNet-34 extracts semantic features at multiple layers
- Features capture high-level facial attributes and characteristics
- Features are saved for advanced matching and analysis

### 3. **Matching Algorithm**
The core matching process uses multiple distance metrics:

#### Step 1: Face Encoding
```python
# User uploads/captures image → generate 128D encoding
user_image = face_recognition.load_image_file(user_image_path)
user_encoding = face_recognition.face_encodings(user_image)[0]
```

#### Step 2: Similarity Calculation
```python
from scipy.spatial.distance import cosine

# Compare with all celebrity encodings
def find_best_match(input_encoding, known_embeddings, known_labels):
    # Calculate cosine distance for each celebrity
    distances = [cosine(input_encoding, emb) for emb in known_embeddings]
    
    # Find celebrity with minimum distance (best match)
    best_match_idx = distances.index(min(distances))
    best_distance = min(distances)
    
    return known_labels[best_match_idx], best_distance

best_match, distance = find_best_match(user_encoding, celebrity_encodings, celebrity_names)
```

#### Step 3: Match Percentage Calculation
```python
# Convert distance to match percentage
match_percentage = (1 - distance) × 100

# Example: distance = 0.06 → Match % = 94.01%
```

### 4. **Result Display**
- PyQt5 interface displays matched celebrity name
- Shows side-by-side comparison with user and celebrity image
- Displays match percentage and similarity metrics
- Provides Save/Share/Delete/Close options
- Allows multiple sequential matches in one session
- Gracefully handles error cases (no face detected)

---

## 📊 Results & Demo

### 🎨 Application Interface

#### Welcome/Home Page
The main welcome screen of CLARA greets users with an intuitive interface featuring:
- **Title Header** - "🌟 FAMOUS FACE-OFF: CELEBS & THEIR SURPRISING LOOKALIKES"
- **Welcome Message** - "👋 Welcome to CLARA 👋" with animated greeting
- **Subtitle** - "Celebrity Look-A-Like Recognition Application"
- **Interactive Buttons:**
  - 📸 **Upload Photo** - Upload image files for face matching
  - 📖 **Manual** - Access user guidance and help documentation
  - **Previous/Next** - Navigation controls for app flow
- **Clara Mascot** - Animated character illustration on the right showcasing facial recognition visualization
- **Beautiful Gradient Background** - Purple gradient theme with professional styling

**Screenshot:**
![CLARA Welcome Page](clara_welcome.jpg)
*Home screen with Clara mascot and interactive upload options*

---

### Real-World Test Cases

#### ✅ Match 1: User Matched to Virat Kohli (94.01% Match)
User image correctly identified as resembling **Virat Kohli** with an impressive **94.01% match score**. The application performed side-by-side comparison showing the striking facial similarities.

**Screenshot:**
![Virat Match 1](virat_match_1.jpg)
*User on the left matched to Virat Kohli (right) with 94.01% similarity*

---

#### ✅ Match 2: User Matched to Virat Kohli (93.78% Match)
Another test case showing consistent high-accuracy matching. User's facial features matched **Virat Kohli** with **93.78% confidence score**, demonstrating the robustness of the matching algorithm.

**Screenshot:**
![Virat Match 2](virat_match_2.jpg)
*User on the left matched to Virat Kohli (right) with 93.78% similarity*

**Real-World Example:** Karthik Sharma, a famous Instagram influencer known for his resemblance to Virat Kohli, was tested with CLARA and correctly matched to Virat Kohli with high confidence!

---

#### ⚠️ Error Handling: No Face Detected
When an uploaded image doesn't contain a detectable human face, CLARA gracefully displays an error message instead of crashing or returning false results.

**Screenshot:**
![No Face Found](no_face_found.jpg)
*Error handling demonstration when image contains no human face*

---

### Summary of Results
| Test Case | Input | Matched Celebrity | Match % | Status |
|---|---|---|---|---|
| Test 1 | User Photo 1 | Virat Kohli | 94.01% | ✅ Success |
| Test 2 | User Photo 2 | Virat Kohli | 93.78% | ✅ Success |
| Test 3 | No-Face Image | N/A | N/A | ✅ Error Handled |
| Real Case | Karthik Sharma | Virat Kohli | High | ✅ Success |

### Matching Accuracy Metrics
- **128D Embeddings** - Deep facial feature representation
- **Cosine Similarity** - Primary matching metric
- **Euclidean Distance** - Secondary distance measure
- **Match Score Calculation** - `Match % = (1 - Distance) × 100`

---

## 🔧 Configuration

### Modify Celebrity Database
To add new celebrities:
1. Create a folder: `Models/data/Celebrity_images/[CelebName]/`
2. Add celebrity images (min 5-10 images recommended)
3. Run: `python Models/face_encoder.py` to regenerate encodings

### Adjust Matching Sensitivity
Edit `Frontend/matcher_utils.py`:
```python
# Cosine distance threshold (0-1)
# Increase threshold to be more strict, decrease to be more lenient
THRESHOLD = 0.6
```

### Change UI Theme
Edit `Frontend/frontend.py` in the `ClaraApp` class:
```python
self.setStyleSheet("""
    QMainWindow {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1A237E, stop:1 #263238);
    }
""")
```

---

## 🎯 Real-World Applications

Beyond being a fun app, CLARA's technology can be adapted for:

✅ **Law Enforcement** - Criminal record matching and identification  
✅ **Identity Verification** - Unique biometric checks in secure systems  
✅ **Duplicate Detection** - Finding similar faces in large datasets  
✅ **Security Systems** - Access control and verification  
✅ **Entertainment** - Celebrity lookalike games and engagement  
✅ **Marketing** - Personalized celebrity-based recommendations  

---

## 🚀 Future Enhancements

- [ ] Web-based interface (Flask/Django + React)
- [ ] Mobile app support (Android/iOS)
- [ ] Group photo detection (multiple faces per image)
- [ ] Celebrity ranking (top 3-5 matches instead of just best match)
- [ ] Historical match tracking and statistics
- [ ] Social media integration (direct share to Instagram/Facebook)
- [ ] Multi-language support (Hindi, Tamil, Telugu, etc.)
- [ ] Real-time performance optimization with GPU acceleration
- [ ] Database integration for user match history
- [ ] Advanced filtering (gender-based, age-based matches)
- [ ] API for third-party integrations

---

## 🐛 Troubleshooting

### Issue: "No face found" error
**Solution:** Ensure image has a clear, front-facing face. Face must be clearly visible and well-lit.

### Issue: Webcam not working
**Solution:** Check camera permissions. On Windows, ensure camera is enabled in Settings → Privacy.

### Issue: Slow matching
**Solution:** This is normal for first-time encoding generation. Subsequent matches are faster (cached embeddings).

### Issue: ModuleNotFoundError for face_recognition
**Solution:**
```bash
pip install --upgrade face-recognition
pip install dlib-bin  # If dlib installation fails
```

---

## 📝 License

This project is open-source and available under the MIT License. Feel free to modify and distribute!

---

## 👥 Team & Development

**CLARA** was developed as a **college final year project** by a 4-member team with professional standards and real-world applications in mind.

### Project Highlights
- **Dataset Creation** - Collected and curated 5000+ images of 110+ Indian celebrities
- **Model Development** - Implemented ResNet-34 CNN and face encoding pipelines
- **Algorithm Design** - Developed cosine similarity and euclidean distance matching
- **GUI Development** - Built complete PyQt5 desktop application with animations
- **Testing & Validation** - Verified with real-world test cases (e.g., Karthik Sharma case)

---

## 📞 Contact & Support

For issues, suggestions, or questions:
- Create an issue on GitHub
- Contact via email or social media 

---

## 🙏 Acknowledgments

- **face_recognition library** - Adam Geitgey (@ageitgey)
- **dlib** - Davis E. King (facial detection and alignment)
- **PyQt5** - Riverbank Computing (GUI framework)
- **PyTorch & torchvision** - Meta AI (deep learning framework)
- **SciPy** - Scientific Python community (cosine similarity calculation)
- **OpenCV** - Intel/Community (video processing)

---

## 📜 License

This project is open-source. Please check the LICENSE file for details.

---

## 🎉 Have Fun!

Discover your Indian celebrity doppelgänger today! Enjoy CLARA and share your surprising matches with friends! 🎬✨

Whether you're a Bollywood fan, sports enthusiast, or just curious about your lookalike, CLARA brings the magic of facial recognition to your desktop – **completely offline, completely private**.

---

**Last Updated:** March 2026  
**Version:** 1.0.0  
**Status:** Stable Release (College Final Year Project)
