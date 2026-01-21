# experiments
My code allows you to automatically search historical newspapers via successive street addresses using the National Library of Australia Trove's API.  You just enter in the street you are searching for, the street numbers you wish to look between, the year span you wish to explore, and your Trove API key and the code does the rest.  

Using the code allows you to automatically search historical newspapers via successive street addresses using Trove's API. 
You just enter in the street you are searching for, the street numbers you wish to look between, the year span you wish to explore, and your Trove API key and the code does the rest.

The code finds newspapers article via your specifications, automatically culls irrelevant results, and creates property and street level CSV files containing article information and full text. The CSV files  are saved to a newly created folder on your computer named after your search terms, i.e. Little_Lonsdale_street_1870_1890.

In addition, the code graphs article frequency by date and street number, displays an on-screen summary of all the articles found on a street level. It produces street level Wordclouds of the most common words in the article text and in the heading text and displays the 20 most common Ngrams on a street level. All of this material is saved to your directory.
The code also attempts to extract all the people mentioned in the articles and adds them to your CSV files. Please note this work's via Stanford University’s Spacy AI that was trained on modern American webcontent. It is not perfect with nineteenth-century material and will often overlook non-American sounding names. As always, machine learning based code reflects the biases of the material it was trained on.

## NEW: Animal Sentiment Analysis Tool

This repository now includes **two notebooks** for tracking emotional attitudes towards animal species in Australian newspapers using machine learning.

### Quick Install

```bash
pip install -r requirements.txt && python -m spacy download en_core_web_sm && python -m textblob.download_corpora
```

Or use the installation script:
- **Linux/Mac**: `./install.sh`
- **Windows**: `install.bat`

See `QUICK_INSTALL.txt` or `INSTALLATION.md` for detailed installation instructions.

### Two Options Available:

#### 1. Basic Notebook (`Animal_Sentiment_Analysis_TROVE.ipynb`)
**Fast & Simple - Good for exploration**
- VADER & TextBlob sentiment analysis (~65% accuracy)
- Process 500 articles in ~10 seconds
- All visualizations included
- No GPU required

#### 2. Advanced Notebook (`Animal_Sentiment_Analysis_Advanced.ipynb`) ⭐
**High Accuracy - Good for research**
- Transformer models: DistilBERT & RoBERTa (~85-90% accuracy)
- **GPU Accelerated**: Process 500 articles in 10-12 minutes (RTX 4070)
- CPU compatible (2-3x slower)
- All visualizations + model comparison

### Features (Both Notebooks):
- Query TROVE API for articles about specific animals (kangaroos, koalas, dingos, etc.)
- Machine learning-based sentiment analysis
- Generate word clouds showing common terms associated with each animal
- Create sentiment trend graphs tracking attitudes over time
- Build geographical heat maps showing sentiment distribution across Australian states
- Export detailed CSV files with full analysis

### Which Should You Use?

| Use Case | Recommended Notebook |
|----------|---------------------|
| Quick exploration | Basic |
| Academic research | Advanced (GPU recommended) |
| Publication-quality | Advanced with RoBERTa |
| < 100 articles | Basic |
| 100+ articles | Advanced |
| No GPU available | Basic (or Advanced on CPU) |

### GPU Performance (Advanced Notebook)

With NVIDIA GPU (RTX 3060 or better):
- **DistilBERT**: 10-12 minutes for 500 articles (85% accuracy)
- **RoBERTa**: 18-20 minutes for 500 articles (90% accuracy)
- Automatic GPU optimization and FP16 mixed precision

### Documentation

- **Quick Start**: See `QUICKSTART.md`
- **Full Guide**: See `ANIMAL_SENTIMENT_ANALYSIS_GUIDE.md`
- **Model Comparison**: See `MODEL_COMPARISON.md` for detailed accuracy and performance benchmarks

---

#have fun,

#Pete 



To successfully run the code, you need an individual TROVE API key. You can acquire a key by signing up as a registered user.
Sign up for Trove here: https://trove.nla.gov.au/
#Once you have signed up:
                        log in to Trove, select your username and select My Profile;
                        select the:  For developers tab;
                        fill in the form to apply for a Trove API key;
                        read the documentation and start using your key to access the API;
                        insert your API key into the code.

The binder link to the code is below.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PeteMina/experiments/main)
