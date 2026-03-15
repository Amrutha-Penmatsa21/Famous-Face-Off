# 📁 Project Folder Structure

## Directory Layout

```
Famous-Face-Off/
│
├── 📂 Frontend/                     # PyQt5 GUI Application
│   ├── frontend.py                  # Main GUI application
│   ├── matcher_utils.py             # Face matching utilities
│   ├── Clara-removebg-preview.png   # Clara mascot image
│   └── TitleCover Page (1).jpg      # Splash screen background
│
├── 📂 Models/                       # ML Models & Matching Logic
│   ├── face_encoder.py              # Generate face encodings
│   ├── feature_extractor.py         # Deep feature extraction (ResNet-34)
│   ├── matcher.py                   # Core matching algorithm
│   ├── utils.py                     # Utility functions
│   │
│   └── 📂 data/
│       ├── 📂 Celebrity_images/     # Celebrity image directories (5000+ images)
│       │   ├── 📂 Aditya_roy_kapoor/
│       │   ├── 📂 Shah_rukh_khan/
│       │   ├── 📂 Priyanka_chopra/
│       │   ├── 📂 MS_Dhoni/
│       │   ├── 📂 Sachin_Tendulkar/
│       │   └── ... (100+ celebrity folders)
│       │
│       ├── embeddings.pkl           # Pre-computed 128D face encodings (Generated)
│       ├── 📂 input_images/         # Test input directory
│       └── 📂 test_images/          # Test dataset
│
├── 📂 docs/                         # Documentation
│   ├── 📂 screenshots/              # Demo screenshots
│   │   ├── clara_welcome.jpg
│   │   ├── virat_match_1.jpg
│   │   ├── virat_match_2.jpg
│   │   └── no_face_found.jpg
│   └── FOLDER_STRUCTURE.md          # This file
│
├── 📄 README.md                     # Main project documentation
├── 📄 SETUP.md                      # Installation & setup guide
├── 📄 CONTRIBUTING.md               # Contribution guidelines
├── 📄 requirements.txt              # Python dependencies
└── 📄 .gitignore                    # Git ignore rules
```

## File Descriptions

### Frontend Files
| File | Purpose |
|------|---------|
| `frontend.py` | Main PyQt5 GUI application with UI components |
| `matcher_utils.py` | Face matching utility functions |
| `Clara-removebg-preview.png` | Clara mascot illustration |
| `TitleCover Page (1).jpg` | Splash screen background image |

### Model Files
| File | Purpose |
|------|---------|
| `face_encoder.py` | Encodes all celebrity faces into 128D vectors |
| `feature_extractor.py` | Extracts deep features using ResNet-34 CNN |
| `matcher.py` | Core matching algorithm (cosine similarity) |
| `utils.py` | Helper functions and utilities |

### Data Directory
| File/Folder | Purpose |
|-------------|---------|
| `Celebrity_images/` | 5000+ celebrity photos in 100+ subfolders |
| `embeddings.pkl` | Pickle file with pre-computed encodings |
| `input_images/` | Test images directory |
| `test_images/` | Test dataset for validation |

### Documentation Files
| File | Purpose |
|------|---------|
| `README.md` | Complete project documentation |
| `SETUP.md` | Installation and setup instructions |
| `CONTRIBUTING.md` | Contribution guidelines |
| `requirements.txt` | Python package dependencies |
| `.gitignore` | Git ignore specifications |

---

## .gitignore - What's Excluded from GitHub

The following are automatically excluded:

```
# Large Data
Models/data/Celebrity_images/    # Too large for GitHub
Models/data/embeddings.pkl       # Generated file
Models/extracted_features/       # Generated output

# Environment Files
venv/                            # Virtual environment
env/                             # Alternative env folder

# Build Artifacts
__pycache__/                     # Python cache
*.pyc                            # Compiled Python
*.spec                           # PyInstaller specs
build/                           # Build output
dist/                            # Distribution files

# IDE Files
.vscode/                         # VS Code settings
.idea/                           # PyCharm settings

# OS Files
.DS_Store                        # Mac system files
Thumbs.db                        # Windows thumbnails
```

---

## How to Set Up This Structure Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/Famous-Face-Off.git
cd Famous-Face-Off

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Generate embeddings (required once)
cd Models
python face_encoder.py
cd ..

# Run the application
cd Frontend
python frontend.py
```

---

## Important Notes

### Large Files (Not in GitHub)
- **Celebrity_images/** - Download separately or generate via script
- **embeddings.pkl** - Generate by running `face_encoder.py`

### Required Before First Run
1. Install dependencies: `pip install -r requirements.txt`
2. Generate embeddings: `python Models/face_encoder.py`
3. Ensure images are in correct paths

### Adding New Celebrities
1. Create folder: `Models/data/Celebrity_images/[Name]/`
2. Add 10+ images
3. Run: `python Models/face_encoder.py`

---

## GitHub Upload Checklist

✅ Cleaned up unnecessary files (venv, __pycache__, etc.)
✅ Updated .gitignore for large files
✅ Organized documentation in docs/ folder
✅ All screenshots moved to docs/screenshots/
✅ Verified requirements.txt
✅ Removed duplicate requirement files
✅ Documented project structure
✅ Ready for GitHub upload

---

**Last Updated:** March 15, 2026
