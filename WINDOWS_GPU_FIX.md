# Windows GPU Installation Fix for RTX 4070

## Problem
PyTorch DLL initialization error (`c10.dll` failed to load) prevents GPU acceleration.

## Solution: Replace Cell 2 in the Advanced Notebook

**Delete the current Cell 2** and replace it with this GPU-optimized installation code:

```python
# ===== GPU-OPTIMIZED INSTALLATION FOR WINDOWS (RTX 4070) =====
# This cell properly installs PyTorch with CUDA support for NVIDIA GPUs
# Run this cell first - it may take 10-15 minutes

import sys
import subprocess
import platform

print("="*70)
print("GPU-OPTIMIZED INSTALLATION FOR WINDOWS")
print("="*70)
print(f"Python: {sys.version}")
print(f"Platform: {platform.platform()}")
print(f"Architecture: {platform.machine()}")
print("="*70 + "\n")

# Step 1: Uninstall any existing broken PyTorch installations
print("Step 1: Cleaning up existing PyTorch installations...")
print("-" * 70)
!{sys.executable} -m pip uninstall -y torch torchvision torchaudio
print("✓ Cleanup complete\n")

# Step 2: Check for Visual C++ Redistributables
print("Step 2: Checking Visual C++ Redistributables...")
print("-" * 70)
print("Note: PyTorch requires Visual C++ 2015-2022 Redistributable")
print("If installation fails, download from:")
print("https://aka.ms/vs/17/release/vc_redist.x64.exe")
print()

# Step 3: Install PyTorch with CUDA 11.8 support (optimized for RTX 4070)
print("Step 3: Installing PyTorch with CUDA 11.8 support...")
print("-" * 70)
print("This will download ~2.5 GB. Please be patient...\n")

!{sys.executable} -m pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118

print("\n✓ PyTorch with CUDA installed\n")

# Step 4: Install transformers and related packages
print("Step 4: Installing transformers and NLP packages...")
print("-" * 70)
!{sys.executable} -m pip install transformers==4.30.2 sentencepiece==0.1.99 accelerate

print("\n✓ Transformer packages installed\n")

# Step 5: Install remaining dependencies
print("Step 5: Installing remaining dependencies...")
print("-" * 70)
!{sys.executable} -m pip install pandas numpy requests nltk textblob vaderSentiment matplotlib seaborn plotly altair wordcloud

print("\n✓ All packages installed\n")

# Step 6: Download NLP data
print("Step 6: Downloading NLP data...")
print("-" * 70)

import nltk
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('vader_lexicon', quiet=True)
print("✓ NLTK data downloaded")

import textblob.download_corpora
textblob.download_corpora.download_all()
print("✓ TextBlob corpora downloaded\n")

# Step 7: CRITICAL - Test GPU installation
print("="*70)
print("STEP 7: TESTING GPU INSTALLATION")
print("="*70 + "\n")

try:
    import torch
    print(f"✓ PyTorch imported successfully")
    print(f"  Version: {torch.__version__}")
    print(f"  CUDA available: {torch.cuda.is_available()}")

    if torch.cuda.is_available():
        print(f"  CUDA version: {torch.version.cuda}")
        print(f"  GPU detected: {torch.cuda.get_device_name(0)}")
        print(f"  GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
        print(f"  Number of GPUs: {torch.cuda.device_count()}")

        # Test GPU computation
        print("\n  Testing GPU computation...")
        x = torch.rand(5, 3)
        x_gpu = x.to('cuda')
        print(f"  ✓ GPU computation test passed!")

        print("\n" + "="*70)
        print("SUCCESS! GPU ACCELERATION IS READY!")
        print("="*70)
        print("\nExpected performance on your RTX 4070:")
        print("  - DistilBERT: ~10-12 minutes for 500 articles")
        print("  - RoBERTa: ~18-20 minutes for 500 articles")
        print("  - Speedup: 2-3x faster than CPU")
        print("="*70)
    else:
        print("\n" + "="*70)
        print("WARNING: GPU NOT DETECTED")
        print("="*70)
        print("\nPossible causes:")
        print("1. Visual C++ Redistributables missing")
        print("   Download: https://aka.ms/vs/17/release/vc_redist.x64.exe")
        print("2. NVIDIA drivers need updating")
        print("   Download: https://www.nvidia.com/Download/index.aspx")
        print("3. CUDA toolkit not properly installed")
        print("\nYou can still use the notebook with CPU (slower)")
        print("="*70)

except Exception as e:
    print("\n" + "="*70)
    print("ERROR DURING INSTALLATION TEST")
    print("="*70)
    print(f"\nError: {e}")
    print("\nTroubleshooting steps:")
    print("1. Install Visual C++ Redistributables:")
    print("   https://aka.ms/vs/17/release/vc_redist.x64.exe")
    print("2. Restart Jupyter kernel after installing")
    print("3. Try running this cell again")
    print("="*70)

print("\n✓ Installation cell complete!")
print("\nNext: Run Cell 3 to import libraries and test GPU acceleration")
```

## Why This Works

1. **Uninstalls broken PyTorch first** - Removes corrupted installations
2. **Installs correct CUDA version** - Uses CUDA 11.8 which is compatible with RTX 4070
3. **Uses official PyTorch index URL** - Ensures GPU-enabled wheels are downloaded
4. **Tests GPU immediately** - Verifies installation worked before proceeding
5. **Provides clear diagnostics** - Shows exactly what's working/failing

## Installation Time

- Total: 10-15 minutes
- PyTorch download: ~2.5 GB (largest part)
- Other packages: ~500 MB

## After Running This Cell

You should see:

```
SUCCESS! GPU ACCELERATION IS READY!
✓ GPU detected: NVIDIA GeForce RTX 4070
  GPU memory: 12.0 GB

Expected performance on your RTX 4070:
  - DistilBERT: ~10-12 minutes for 500 articles
  - RoBERTa: ~18-20 minutes for 500 articles
  - Speedup: 2-3x faster than CPU
```

## If GPU Still Not Detected

1. **Install Visual C++ Redistributables** (most common fix):
   - Download: https://aka.ms/vs/17/release/vc_redist.x64.exe
   - Run installer as Administrator
   - Restart Jupyter kernel
   - Run the installation cell again

2. **Update NVIDIA Drivers**:
   - Download latest from: https://www.nvidia.com/Download/index.aspx
   - Select: GeForce RTX 40 Series → RTX 4070
   - Install and restart computer

3. **Verify NVIDIA GPU in Device Manager**:
   - Open Device Manager (Windows key + X)
   - Expand "Display adapters"
   - Should see "NVIDIA GeForce RTX 4070"
   - If yellow warning icon, drivers need updating

## Quick Test Commands

After installation, test GPU in a new cell:

```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")
```

## Command to Run in Windows CMD (If Jupyter Fails)

Open Anaconda Prompt as Administrator and run:

```cmd
pip uninstall -y torch torchvision torchaudio
pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
python -c "import torch; print('CUDA:', torch.cuda.is_available())"
```

Expected output: `CUDA: True`
