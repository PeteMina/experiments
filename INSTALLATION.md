# Installation Guide - Animal Sentiment Analysis TROVE

## Quick Install (All Packages)

### Option 1: Install from requirements.txt (Recommended)

```bash
pip install -r requirements.txt
```

### Option 2: Install all packages directly

```bash
pip install altair==4.1.0 nltk==3.6.1 pandas==1.2.4 requests==2.25.1 spacy==3.1.3 textblob==0.17.1 vega==3.5.0 wordcloud==1.8.1 vaderSentiment==3.3.2 plotly==5.3.1 seaborn==0.11.2 matplotlib==3.4.3 numpy==1.21.0 transformers==4.30.2 torch==2.0.1 sentencepiece==0.1.99
```

---

## Step-by-Step Installation

### 1. Core Dependencies (Required for both notebooks)

```bash
pip install pandas==1.2.4 numpy==1.21.0 requests==2.25.1
```

### 2. Sentiment Analysis Libraries

```bash
pip install textblob==0.17.1 vaderSentiment==3.3.2 nltk==3.6.1
```

### 3. Visualization Libraries

```bash
pip install matplotlib==3.4.3 seaborn==0.11.2 plotly==5.3.1 altair==4.1.0 vega==3.5.0 wordcloud==1.8.1
```

### 4. NLP Libraries (for basic notebook entity extraction)

```bash
pip install spacy==3.1.3
python -m spacy download en_core_web_sm
```

### 5. Advanced ML Libraries (for advanced notebook with transformers)

**For GPU support (NVIDIA GPU required):**
```bash
pip install torch==2.0.1 transformers==4.30.2 sentencepiece==0.1.99
```

**For CPU only:**
```bash
pip install torch==2.0.1+cpu transformers==4.30.2 sentencepiece==0.1.99 -f https://download.pytorch.org/whl/torch_stable.html
```

### 6. Download Required Data Files

```bash
python -m textblob.download_corpora
python -m nltk.downloader stopwords punkt averaged_perceptron_tagger vader_lexicon
```

---

## Installation by Notebook

### For Basic Notebook Only

If you only need the basic notebook (`Animal_Sentiment_Analysis_TROVE.ipynb`):

```bash
pip install pandas==1.2.4 numpy==1.21.0 requests==2.25.1 textblob==0.17.1 vaderSentiment==3.3.2 nltk==3.6.1 matplotlib==3.4.3 seaborn==0.11.2 plotly==5.3.1 altair==4.1.0 vega==3.5.0 wordcloud==1.8.1 spacy==3.1.3

# Download required data
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
python -m nltk.downloader stopwords punkt averaged_perceptron_tagger vader_lexicon
```

### For Advanced Notebook (with GPU)

For the advanced notebook with GPU acceleration:

```bash
pip install pandas==1.2.4 numpy==1.21.0 requests==2.25.1 textblob==0.17.1 vaderSentiment==3.3.2 nltk==3.6.1 matplotlib==3.4.3 seaborn==0.11.2 plotly==5.3.1 altair==4.1.0 vega==3.5.0 wordcloud==1.8.1 torch==2.0.1 transformers==4.30.2 sentencepiece==0.1.99

# Download required data
python -m textblob.download_corpora
python -m nltk.downloader stopwords punkt averaged_perceptron_tagger vader_lexicon
```

---

## GPU-Specific Installation

### NVIDIA GPU (CUDA Support)

For GPU acceleration with CUDA (RTX 3060, 3080, 4070, 4090, etc.):

```bash
# Install PyTorch with CUDA 11.8 support
pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118

# Install transformers and dependencies
pip install transformers==4.30.2 sentencepiece==0.1.99
```

### Verify GPU Installation

```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"GPU name: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'N/A'}")
```

Expected output for RTX 4070:
```
CUDA available: True
GPU name: NVIDIA GeForce RTX 4070
```

---

## Troubleshooting

### "No module named 'torch'"

If PyTorch installation fails:

```bash
# Try with specific CUDA version
pip install torch==2.0.1+cu118 --extra-index-url https://download.pytorch.org/whl/cu118

# Or for CPU only
pip install torch==2.0.1+cpu --extra-index-url https://download.pytorch.org/whl/cpu
```

### "No module named 'transformers'"

```bash
pip install --upgrade transformers
```

### "CUDA out of memory"

Your GPU may not have enough VRAM. In the advanced notebook, reduce batch size:

```python
BATCH_SIZE = 16  # Instead of 24
```

### Spacy model download fails

```bash
# Try direct download
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.1.0/en_core_web_sm-3.1.0-py3-none-any.whl
```

### Import errors with plotly

```bash
pip install --upgrade plotly kaleido
```

---

## Virtual Environment Setup (Recommended)

### Using venv

```bash
# Create virtual environment
python -m venv trove_env

# Activate (Windows)
trove_env\Scripts\activate

# Activate (Mac/Linux)
source trove_env/bin/activate

# Install all requirements
pip install -r requirements.txt

# Download data files
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
python -m nltk.downloader stopwords punkt averaged_perceptron_tagger vader_lexicon
```

### Using conda

```bash
# Create conda environment
conda create -n trove_env python=3.9

# Activate
conda activate trove_env

# Install PyTorch with CUDA (for GPU)
conda install pytorch==2.0.1 torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# Install other requirements
pip install -r requirements.txt

# Download data files
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
python -m nltk.downloader stopwords punkt averaged_perceptron_tagger vader_lexicon
```

---

## Complete Setup Script

### For Linux/Mac

```bash
#!/bin/bash

# Create and activate virtual environment
python3 -m venv trove_env
source trove_env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt

# Download required data files
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
python -m nltk.downloader stopwords punkt averaged_perceptron_tagger vader_lexicon

# Verify GPU (optional)
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"

echo "Installation complete!"
```

Save as `setup.sh` and run:
```bash
chmod +x setup.sh
./setup.sh
```

### For Windows

```batch
@echo off

REM Create and activate virtual environment
python -m venv trove_env
call trove_env\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip

REM Install all requirements
pip install -r requirements.txt

REM Download required data files
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
python -m nltk.downloader stopwords punkt averaged_perceptron_tagger vader_lexicon

REM Verify GPU
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"

echo Installation complete!
pause
```

Save as `setup.bat` and double-click to run.

---

## Package Sizes and Download Times

Estimated download sizes:
- Basic packages: ~150 MB
- With transformers: ~500 MB
- With PyTorch + CUDA: ~2.5 GB

On a fast connection:
- Basic install: ~2-3 minutes
- Full install with GPU: ~5-10 minutes

---

## Verification Script

After installation, verify everything works:

```python
# test_installation.py

import sys

def test_imports():
    """Test if all required packages can be imported."""
    packages = [
        'pandas', 'numpy', 'requests',
        'nltk', 'textblob', 'vaderSentiment',
        'matplotlib', 'seaborn', 'plotly', 'altair',
        'wordcloud', 'spacy',
        'torch', 'transformers', 'sentencepiece'
    ]

    failed = []
    for package in packages:
        try:
            __import__(package)
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package} - FAILED")
            failed.append(package)

    if failed:
        print(f"\nFailed imports: {', '.join(failed)}")
        print("Run: pip install " + " ".join(failed))
    else:
        print("\n✓ All packages installed successfully!")

    # Check GPU
    try:
        import torch
        if torch.cuda.is_available():
            print(f"\n✓ GPU detected: {torch.cuda.get_device_name(0)}")
            print(f"  VRAM: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
        else:
            print("\n⚠ No GPU detected (CPU only)")
    except:
        pass

if __name__ == "__main__":
    test_imports()
```

Run with:
```bash
python test_installation.py
```

---

## System Requirements

### Minimum Requirements (Basic Notebook)
- Python 3.7+
- 4 GB RAM
- 500 MB disk space

### Recommended Requirements (Advanced Notebook)
- Python 3.8+
- 16 GB RAM
- NVIDIA GPU with 8+ GB VRAM (RTX 3060 or better)
- 5 GB disk space
- CUDA 11.8+

### Optimal Setup
- Python 3.9 or 3.10
- 32 GB RAM
- NVIDIA RTX 4070 or better (12+ GB VRAM)
- 10 GB disk space
- CUDA 11.8 or 12.x

---

## Quick Reference

**Install everything:**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
```

**Verify installation:**
```bash
python -c "import torch; print('GPU:', torch.cuda.is_available())"
```

**Start Jupyter:**
```bash
jupyter notebook
```

That's it! You're ready to analyze sentiment in Australian newspapers! 🦘
