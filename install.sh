#!/bin/bash
# Quick installation script for Animal Sentiment Analysis TROVE

echo "=========================================="
echo "Animal Sentiment Analysis - Installation"
echo "=========================================="
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install all requirements
echo ""
echo "Installing all packages from requirements.txt..."
pip install -r requirements.txt

# Download spacy model
echo ""
echo "Downloading spacy English model..."
python -m spacy download en_core_web_sm

# Download textblob corpora
echo ""
echo "Downloading TextBlob corpora..."
python -m textblob.download_corpora

# Download NLTK data
echo ""
echo "Downloading NLTK data..."
python -m nltk.downloader stopwords punkt averaged_perceptron_tagger vader_lexicon

# Verify installation
echo ""
echo "=========================================="
echo "Verifying installation..."
echo "=========================================="
python -c "
import pandas, numpy, requests
import nltk, textblob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib, seaborn, plotly, altair
from wordcloud import WordCloud
import spacy
import torch, transformers, sentencepiece

print('✓ All basic packages installed successfully!')

if torch.cuda.is_available():
    print(f'✓ GPU detected: {torch.cuda.get_device_name(0)}')
    print(f'  VRAM: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB')
else:
    print('⚠ No GPU detected (CPU mode)')
    print('  Advanced notebook will run slower without GPU')
"

echo ""
echo "=========================================="
echo "Installation complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Get your TROVE API key from https://trove.nla.gov.au/"
echo "2. Run: jupyter notebook"
echo "3. Open Animal_Sentiment_Analysis_TROVE.ipynb (basic)"
echo "   or Animal_Sentiment_Analysis_Advanced.ipynb (advanced)"
echo ""
