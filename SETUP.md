# 🛠️ CLARA - Setup & Installation Guide

## Prerequisites
- **Python 3.7+** (Recommended: Python 3.10 or 3.11)
- **pip** (Python package manager)
- **Git** (for cloning the repository)
- **2GB+ storage** (for celebrity database and models)
- **Webcam** (optional, for real-time matching)

---

## ⚡ Quick Start (Windows)

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/Famous-Face-Off.git
cd Famous-Face-Off
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Generate Face Encodings (First Time Only)
```bash
cd Models
python face_encoder.py
cd ..
```

### Step 5: Run the Application
```bash
cd Frontend
python frontend.py
```

---

## 🐧 Setup (Linux/Mac)

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/Famous-Face-Off.git
cd Famous-Face-Off
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Generate Face Encodings
```bash
cd Models
python3 face_encoder.py
cd ..
```

### Step 5: Run the Application
```bash
cd Frontend
python3 frontend.py
```

---

## 🔧 Troubleshooting

### Issue: "No module named 'face_recognition'"
```bash
pip install face_recognition
pip install dlib-bin
```

### Issue: "Could not open webcam"
- Check camera permissions in system settings
- Ensure no other app is using the camera
- Try restarting the application

### Issue: "embeddings.pkl not found"
```bash
cd Models
python face_encoder.py
```

### Issue: "Image not found" on startup
- Ensure images are in the correct paths
- Check [Frontend/Clara-removebg-preview.png](Frontend/Clara-removebg-preview.png)
- Check [Frontend/TitleCover Page (1).jpg](Frontend/TitleCover%20Page%20(1).jpg)

---

## 📦 Dependencies

See [requirements.txt](requirements.txt) for the complete list of dependencies.

Key packages:
- **PyQt5** - GUI Framework
- **face_recognition** - Face encoding (dlib)
- **OpenCV** - Video capture and processing
- **PyTorch & torchvision** - Deep learning
- **Pillow** - Image processing
- **scipy** - Distance calculations

---

## 🎓 Project Structure

```
Famous-Face-Off/
├── Frontend/              # GUI Application
│   ├── frontend.py
│   ├── matcher_utils.py
│   └── requirements.txt   (install from root requirements.txt)
│
├── Models/                # ML & Matching Logic
│   ├── face_encoder.py    # Generate embeddings
│   ├── feature_extractor.py
│   ├── matcher.py
│   ├── utils.py
│   └── data/
│       ├── Celebrity_images/  (5000+ images, 110+ celebrities)
│       ├── embeddings.pkl     (Generated after face_encoder.py)
│       ├── input_images/
│       └── test_images/
│
├── docs/                  # Documentation
│   └── screenshots/       # Demo screenshots
│
├── requirements.txt       # All dependencies
├── README.md             # Main documentation
├── SETUP.md              # This file
└── .gitignore            # Git ignore rules
```

---

## 🚀 Next Steps

1. Read [README.md](README.md) for full documentation
2. Check [docs/screenshots/](docs/screenshots/) for demo images
3. Explore [Models/](Models/) for ML implementation details
4. Start with [Frontend/frontend.py](Frontend/frontend.py)

---

## ❓ Questions?

- Check README.md for detailed information
- Review the code comments


Happy matching! 🎬✨
