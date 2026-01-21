# Installation Instructions for Jupyter Labs/Notebook

## ⚠️ WINDOWS USERS WITH GPU

If you're on Windows with an NVIDIA GPU (RTX 4070, RTX 3080, etc.) and want GPU acceleration, **use the installation cell in the Advanced Notebook** instead of these manual steps. It includes:
- Proper PyTorch with CUDA support
- Automatic GPU detection and testing
- Visual C++ dependency checks
- See `WINDOWS_GPU_FIX.md` for troubleshooting

## Run These Commands in Jupyter Cells

### Cell 1: Install all packages from requirements.txt

```python
import sys
!{sys.executable} -m pip install -r requirements.txt
```

### Cell 2: Download Spacy model

```python
import sys
!{sys.executable} -m spacy download en_core_web_sm
```

### Cell 3: Download TextBlob corpora

```python
import sys
!python -m textblob.download_corpora
```

### Cell 4: Download NLTK data

```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')
```

### Cell 5: Verify installation

```python
# Test imports
import pandas, numpy, requests
import nltk, textblob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib, seaborn, plotly, altair
from wordcloud import WordCloud
import spacy
import torch, transformers, sentencepiece

print("✓ All packages installed successfully!")

# Check GPU
if torch.cuda.is_available():
    print(f"✓ GPU detected: {torch.cuda.get_device_name(0)}")
    print(f"  VRAM: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
else:
    print("⚠ No GPU detected (CPU mode)")
```

---

## One-Cell Installation (Alternative)

If you prefer, you can run everything in one cell:

```python
import sys

# Install all packages
print("Installing packages from requirements.txt...")
!{sys.executable} -m pip install -r requirements.txt

# Download spacy model
print("\nDownloading Spacy model...")
!{sys.executable} -m spacy download en_core_web_sm

# Download textblob corpora
print("\nDownloading TextBlob corpora...")
!{sys.executable} -m python -m textblob.download_corpora

# Download NLTK data
print("\nDownloading NLTK data...")
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')

print("\n✓ Installation complete!")
```

---

## Important Notes

1. **Use `!{sys.executable}` not just `!pip`** - This ensures you're installing to the correct Python environment
2. **Run cells in order** - Some commands depend on previous installations
3. **Restart kernel after installation** - Go to Kernel → Restart Kernel after installing
4. **Check for errors** - If a cell fails, read the error message and try again

---

## If Installation Fails

### Common Issues:

**"Could not find requirements.txt"**
- Make sure you're in the correct directory
- In Jupyter, run: `!pwd` to see current directory
- Navigate to the project folder first

**"Permission denied"**
- Try: `!{sys.executable} -m pip install --user -r requirements.txt`

**"No module named 'pip'"**
- Run: `!python -m ensurepip --upgrade`

**Torch/CUDA issues**
- For GPU support: `!pip install torch==2.0.1 --index-url https://download.pytorch.org/whl/cu118`
- For CPU only: `!pip install torch==2.0.1 --index-url https://download.pytorch.org/whl/cpu`

---

## Quick Test After Installation

Run this in a Jupyter cell:

```python
# Quick test
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

import transformers
print(f"Transformers version: {transformers.__version__}")

import pandas as pd
print(f"Pandas version: {pd.__version__}")

print("\n✓ Everything is working!")
```
