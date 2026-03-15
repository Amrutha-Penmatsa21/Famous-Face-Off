# 📊 Celebrity Dataset

## What You Need to Know

The CLARA application requires a **celebrity dataset (110+ celebrities, 5000+ images, ~1-2GB)** to function. 

**Why separate?**
- ✅ Keeps GitHub repo small (5MB, not 2GB)
- ✅ Faster to clone and setup
- ✅ Better licensing management
- ✅ Easy to update independently

---

## How to Get the Dataset

### Option 1: Email Request (Recommended)

Send email to: **[amruthaamrutha322@gmail.com]**

**Subject:** `Dataset Request - CLARA`

**Include:**
- Your name
- How you plan to use CLARA
- Your GitHub username

### Option 2: GitHub Issue

Create an issue with title: `Dataset Request`

Include your name and intended use case

---

## After You Receive the Dataset

### Step 1: Extract Files
```
Extract dataset to:
Models/data/Celebrity_images/
```

### Step 2: Generate Encodings
```bash
cd Models
python face_encoder.py
```
This takes ~20-40 minutes (one-time only)

### Step 3: Run Application
```bash
cd Frontend
python frontend.py
```

Done! ✅

---

## Dataset Contents

**110+ Indian Celebrities:**
- Bollywood: Shah Rukh Khan, Priyanka Chopra, Deepika Padukone, etc.
- Sports: Virat Kohli, MS Dhoni, Sachin Tendulkar, etc.
- Tollywood & Regional: Prabhas, Mahesh Babu, Ram Charan, etc.
- Tamil/Telugu: Rajinikanth, Surya, Dhanush, etc.
- Music: Arijit Singh, Shreya Ghoshal, etc.

**Total:** 50+ images per celebrity = 5,000+ images

---

## Folder Structure

```
Models/data/
├── Celebrity_images/
│   ├── Shah_rukh_khan/
│   ├── Virat_Kohli/
│   ├── Priyanka_Chopra/
│   └── ... (110+ celebrities)
├── embeddings.pkl          (Generated automatically)
├── input_images/
└── test_images/
```

---

## FAQ

**Q: Why not just post the dataset on GitHub?**  
A: It's 1-2GB - way too large. GitHub repos should stay under 100MB.

**Q: How long does face encoding take?**  
A: 20-40 minutes on average PC. It's a one-time process.

**Q: Can I add more celebrities?**  
A: Yes! Create a new folder with celebrity images, then re-run `face_encoder.py`.

**Q: What image formats work?**  
A: JPG, PNG, and common formats. Needs clear, front-facing faces.

**Q: How long to get approval?**  
A: Usually 1-2 days if it's for legitimate use (portfolio, learning, research).

**Q: Can I share the dataset?**  
A: No - it's for your personal use only. Others should request separately.

---

## Quick Links

- 📖 [README.md](README.md) - Full project documentation
- 🚀 [SETUP.md](SETUP.md) - Installation guide
- 🤝 [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

---

**Last Updated:** March 15, 2026
