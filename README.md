# experiments
My code allows you to automatically search historical newspapers via successive street addresses using the National Library of Australia Trove's API.  You just enter in the street you are searching for, the street numbers you wish to look between, the year span you wish to explore, and your Trove API key and the code does the rest.  

Using the code allows you to automatically search historical newspapers via successive street addresses using Trove's API. 
You just enter in the street you are searching for, the street numbers you wish to look between, the year span you wish to explore, and your Trove API key and the code does the rest.

The code finds newspapers article via your specifications, automatically culls irrelevant results, and creates property and street level CSV files containing article information and full text. The CSV files  are saved to a newly created folder on your computer named after your search terms, i.e. Little_Lonsdale_street_1870_1890.

In addition, the code graphs article frequency by date and street number, displays an on-screen summary of all the articles found on a street level. It produces street level Wordclouds of the most common words in the article text and in the heading text and displays the 20 most common Ngrams on a street level. All of this material is saved to your directory.
The code also attempts to extract all the people mentioned in the articles and adds them to your CSV files. Please note this work's via Stanford University’s Spacy AI that was trained on modern American webcontent. It is not perfect with nineteenth-century material and will often overlook non-American sounding names. As always, machine learning based code reflects the biases of the material it was trained on.

## NEW: Animal Sentiment Analysis Tool

This repository now includes `Animal_Sentiment_Analysis_TROVE.ipynb` - a comprehensive tool for tracking emotional attitudes towards animal species in Australian newspapers using machine learning.

### Features:
- Query TROVE API for articles about specific animals (kangaroos, koalas, dingos, etc.)
- Machine learning-based sentiment analysis using TextBlob and VADER
- Generate word clouds showing common terms associated with each animal
- Create sentiment trend graphs tracking attitudes over time
- Build geographical heat maps showing sentiment distribution across Australian states
- Export detailed CSV files with full analysis

See `ANIMAL_SENTIMENT_ANALYSIS_GUIDE.md` for complete documentation and usage instructions.

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
