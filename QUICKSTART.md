# Quick Start Guide - Animal Sentiment Analysis

## Get Started in 3 Steps

### Step 1: Get Your API Key
1. Go to https://trove.nla.gov.au/
2. Sign up or log in
3. Profile → "For developers" → Request API key
4. Copy your API key

### Step 2: Choose Your Method

#### Option A: Jupyter Notebook (Recommended for exploration)
```bash
# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook Animal_Sentiment_Analysis_TROVE.ipynb

# In the notebook:
# 1. Insert your API key in the config cell
# 2. Run all cells
```

#### Option B: Python Script (For quick analysis)
```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python animal_sentiment_analysis.py

# Enter your API key when prompted
```

### Step 3: View Results

Results are saved to `animal_sentiment_YYYY_YYYY/` directory:

**CSV Files:**
- `all_animals_sentiment_*.csv` - Complete dataset
- `{animal}_sentiment_*.csv` - Individual animal data
- `summary_statistics_*.csv` - Aggregated metrics

**Visualizations:**
- `wordcloud_*.png` - Word clouds for each animal
- `sentiment_trends.html` - Interactive trend graphs
- `sentiment_heatmap.png` - Geographic sentiment distribution

---

## Advanced Option: Higher Accuracy with GPU

**Want 85-90% accuracy instead of 60-65%?** Use the advanced notebook!

### Quick Comparison

| Feature | Basic Notebook | Advanced Notebook |
|---------|----------------|-------------------|
| **Accuracy** | ~65% (VADER) | ~85-90% (Transformers) |
| **Speed** | 10 seconds | GPU: 10-12 min / CPU: 25 min |
| **Models** | VADER, TextBlob | DistilBERT, RoBERTa |
| **Best For** | Quick exploration | Research, publications |
| **GPU Needed** | No | Recommended (2-3x faster) |

### When to Use Advanced

✅ **Use Advanced if:**
- Need high accuracy (research, publication)
- Have GPU (RTX 3060 or better)
- Processing 100+ articles
- Analyzing complex historical text

❌ **Stick with Basic if:**
- Quick exploration only
- Processing < 100 articles
- No GPU and time-constrained
- Just need rough estimates

### How to Use Advanced

Same 3 steps, just open the advanced notebook:

```bash
jupyter notebook Animal_Sentiment_Analysis_Advanced.ipynb
```

**Automatic GPU optimization:**
- Detects your GPU automatically
- Sets optimal batch size (24 for RTX 4070)
- Enables FP16 for 40% speedup
- Shows real-time progress

**Example Performance (RTX 4070):**
- DistilBERT: 10-12 minutes for 500 articles (85% accuracy)
- RoBERTa: 18-20 minutes for 500 articles (90% accuracy)

### Model Selection

In the advanced notebook, choose your model:

```python
SENTIMENT_MODEL = 'distilbert'  # Recommended (fast + accurate)
# or 'roberta'  # Highest accuracy (slower)
# or 'all'  # Compare all models
```

**Recommendation:** Start with `distilbert` - best balance of speed and accuracy.

### See Full Comparison

For detailed model comparison, GPU requirements, and performance benchmarks:
- Read `MODEL_COMPARISON.md`

---

## Example Output

```
Average sentiment by animal:
  Platypus     : +0.245 (POSITIVE)
  Koala        : +0.156 (POSITIVE)
  Wombat       : +0.089 (NEUTRAL)
  Kangaroo     : +0.034 (NEUTRAL)
  Dingo        : -0.112 (NEGATIVE)
  Snake        : -0.187 (NEGATIVE)
  Crocodile    : -0.203 (NEGATIVE)
  Shark        : -0.289 (NEGATIVE)
```

## Customize Your Analysis

### Different Animals
```python
animals = ['echidna', 'tasmanian devil', 'quoll', 'bilby']
```

### Different Time Period
```python
start_year = 1850
end_year = 1900
```

### Specific States
```python
states = ['Victoria', 'New South Wales']
```

### More Articles
```python
max_articles_per_animal = 1000
```

## What You Get

### 1. Sentiment Scores
- **VADER Compound**: -1 (very negative) to +1 (very positive)
- **Polarity**: Overall emotional tone
- **Subjectivity**: How opinionated vs factual

### 2. Word Clouds
- See most common words associated with each animal
- Separate clouds for positive vs negative articles
- Identify key themes and language patterns

### 3. Trend Graphs
- Track sentiment changes over decades
- Compare multiple animals on same chart
- Interactive: hover for details

### 4. Heat Maps
- **Geographic**: Sentiment by Australian state
- **Temporal**: Sentiment by year and month
- Reveals regional and seasonal patterns

## Example Research Workflows

### Research Question: "How did WWI affect attitudes towards dingos?"
```python
animals = ['dingo']
start_year = 1910
end_year = 1920
```

### Research Question: "Regional differences in shark sentiment"
```python
animals = ['shark']
states = []  # All states
start_year = 1900
end_year = 1950
# Then examine the geographic heatmap
```

### Research Question: "Compare native vs introduced species"
```python
animals = ['kangaroo', 'koala', 'rabbit', 'fox', 'cat']
start_year = 1850
end_year = 1950
```

## Troubleshooting

**"No results found"**
- Check API key is correct
- Try different animals or date ranges
- Lower `min_relevance_score`

**"Memory error"**
- Reduce `max_articles_per_animal`
- Process fewer animals at once

**Visualizations not showing**
- Make sure all packages installed: `pip install -r requirements.txt`
- Run cells in order from top to bottom

## Need More Help?

See `ANIMAL_SENTIMENT_ANALYSIS_GUIDE.md` for complete documentation.

## Have Fun!

This tool opens up fascinating insights into how Australian society viewed wildlife over time. Explore, experiment, and discover!
