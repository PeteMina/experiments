@echo off
REM Quick installation script for Animal Sentiment Analysis TROVE

echo ==========================================
echo Animal Sentiment Analysis - Installation
echo ==========================================
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install all requirements
echo.
echo Installing all packages from requirements.txt...
pip install -r requirements.txt

REM Download spacy model
echo.
echo Downloading spacy English model...
python -m spacy download en_core_web_sm

REM Download textblob corpora
echo.
echo Downloading TextBlob corpora...
python -m textblob.download_corpora

REM Download NLTK data
echo.
echo Downloading NLTK data...
python -m nltk.downloader stopwords punkt averaged_perceptron_tagger vader_lexicon

REM Verify installation
echo.
echo ==========================================
echo Verifying installation...
echo ==========================================
python -c "import pandas, numpy, requests; import nltk, textblob; from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer; import matplotlib, seaborn, plotly, altair; from wordcloud import WordCloud; import spacy; import torch, transformers, sentencepiece; print('✓ All basic packages installed successfully!'); print(f'✓ GPU detected: {torch.cuda.get_device_name(0)}' if torch.cuda.is_available() else '⚠ No GPU detected (CPU mode)')"

echo.
echo ==========================================
echo Installation complete!
echo ==========================================
echo.
echo Next steps:
echo 1. Get your TROVE API key from https://trove.nla.gov.au/
echo 2. Run: jupyter notebook
echo 3. Open Animal_Sentiment_Analysis_TROVE.ipynb (basic)
echo    or Animal_Sentiment_Analysis_Advanced.ipynb (advanced)
echo.
pause
