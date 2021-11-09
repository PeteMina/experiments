# experiments
This code allows you to automatically search historical newspapers via successive street addresses using the National Library of Australia Trove's API.  You just enter in the street you are searching for, the street numbers you wish to look between, the year span you wish to explore, and your Trove API key and the code does the rest.  

This code allows you to automatically search historical newspapers via successive street addresses using Trove's API. 
You just enter in the street you are searching for, the street numbers you wish to look between, the year span you wish to explore, and your Trove API key and the code does the rest.

The code finds newspapers article via your specifications, automatically culls irrelevant results, and creates property and street level CSV files containing article information and full text. The CSV files  are saved to a newly created folder on your computer named after your search terms, i.e. Little_Lonsdale_street_1870_1890.

In addition, the code graphs article frequency by date and street number, displays an on-screen summary of all the articles found on a street level. It produces street level Wordclouds of the most common words in the article text and in the heading text and displays the 20 most common Ngrams on a street level. All of this material is saved to your directory.
The code also attempts to extract all the people mentioned in the articles and adds them to your CSV files. Please note this work's via Stanford University’s Spacy AI that was trained on modern American webcontent. It is not perfect with nineteenth-century material and will often overlook non-American sounding names. As always, machine learning based code reflects the biases of the material it was trained on.

#have fun,

#Pete 



To successfully run the code, you need an individual TROVE API key. You can acquire a key by signing up as a registered user.
Sign up for Trove here: https://trove.nla.gov.au/
#Once you have signed up:
                        log in to Trove, select your username and select My Profile;
                        select the:  For developers tab;
                        fill in the form to apply for a Trove API key;
                        read the documentation and start using your key to access the API;
                        insert your API key into the code below as instructed.
https://hub.gke2.mybinder.org/user/petemina-experiments-tmitauka/lab/tree/Trawl%20Trove%20by%20Street%20Numbers%2C%20fully%20featured%20.ipynb
