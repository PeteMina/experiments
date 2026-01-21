# TROVE Animal Sentiment Analyzer - Quick Start Guide

## NEW: Streamlined Version

The **Animal_Sentiment_Analysis_Streamlined.ipynb** notebook is a simplified, user-friendly version that:

✓ **Smart Installation** - Only installs missing packages
✓ **Silent GPU Setup** - Automatically detects and configures GPU (only reports if problems)
✓ **Interactive Prompts** - Easy-to-use inputs for all settings
✓ **RoBERTa Model** - High accuracy (90%) sentiment analysis
✓ **Complete Outputs** - All visualizations and data from original version

## How to Use

### Step 1: Get a TROVE API Key (Free)

1. Visit: https://trove.nla.gov.au/about/create-something/using-api
2. Click "Request an API key"
3. Fill out the form (instant approval)
4. Copy your API key

### Step 2: Open the Notebook

Open **Animal_Sentiment_Analysis_Streamlined.ipynb** in Jupyter Labs/Notebook

### Step 3: Run the Cells

#### Cell 1: Setup (5-15 minutes first time)
- Automatically installs any missing packages
- Detects and configures your GPU
- First run downloads ~2.5 GB for GPU support

**Expected output:**
```
✓ GPU Acceleration: ENABLED (NVIDIA GeForce RTX 4070, 12.0GB)
✓ Optimized batch size: 24
✓ Expected speed: 2-3x faster than CPU
```

#### Cell 2: Configuration
You'll be prompted for:

1. **TROVE API key** - Paste your key from Step 1
2. **Animals** - Enter comma-separated list
   - Example: `kangaroo, koala, dingo, platypus, wombat`
3. **Date range** - Start and end years
   - Example: `1900` to `1950`
4. **Location** - Choose from:
   - Option 1: All of Australia
   - Option 2: Specific states (NSW, VIC, QLD, SA, WA, TAS, NT, ACT)
   - Option 3: Specific newspapers (enter IDs)
5. **Article count** - How many articles per animal
   - Recommended: 50-200 for quick analysis, 500+ for comprehensive

**Example interaction:**
```
Enter your TROVE API key: abc123def456...
✓ API key accepted

Enter animals to analyze (comma-separated):
> kangaroo, koala, wombat

Enter date range:
  Start year (e.g., 1900): 1900
  End year (e.g., 1950): 1950
✓ Date range: 1900 to 1950

Location filter options:
1. All of Australia (no filter)
2. Specific state(s)
3. Specific newspaper(s)
Choose option (1/2/3): 2

Enter state codes (comma-separated):
Options: NSW, VIC, QLD, SA, WA, TAS, NT, ACT
> NSW, VIC
✓ Filtering by states: NSW, VIC

How many articles per animal?
Articles per animal (default 100): 200
✓ Will retrieve up to 200 articles per animal
```

#### Cell 3: Load RoBERTa Model (1-2 minutes)
- Automatically loads the RoBERTa sentiment model
- First time downloads ~500 MB model files
- GPU optimization applied automatically

#### Cell 4: Helper Functions
- Just run it (defines internal functions)

#### Cell 5: Retrieve & Analyze
- Queries TROVE API for your articles
- Performs GPU-accelerated sentiment analysis
- Shows real-time progress with ETA

**Expected output:**
```
Querying TROVE for 'kangaroo'... Retrieved 200 articles
Querying TROVE for 'koala'... Retrieved 195 articles
Querying TROVE for 'wombat'... Retrieved 187 articles

✓ Total articles collected: 582

Analyzing 582 articles with RoBERTa...
Batch size: 24 | Device: GPU | FP16: True
Progress: 100% (582/582) | 48.5 articles/sec | ETA: 0.0min
✓ Completed in 0.2 minutes (48.33 articles/sec)
  Peak VRAM usage: 3.42 GB

Average sentiment by animal:
--------------------------------------------------
Koala          : +0.456 [POSITIVE] ████████████████████████
Kangaroo       : +0.234 [POSITIVE] ████████████
Wombat         : -0.123 [NEGATIVE] ██████
```

#### Cell 6: Visualizations
- Generates all visualizations automatically
- Saves files to disk

## What You Get

### Generated Files:

1. **wordclouds_1900_1950.png** - Word clouds for each animal
2. **sentiment_comparison_1900_1950.png** - Bar chart comparing animals
3. **sentiment_trends_1900_1950.html** - Interactive timeline (open in browser)
4. **sentiment_heatmap_1900_1950.png** - Heat map by year and animal
5. **sentiment_distribution_1900_1950.png** - Distribution charts
6. **animal_sentiment_results_1900_1950.csv** - Full dataset with all articles
7. **sentiment_summary_1900_1950.csv** - Summary statistics

### Visualizations Include:

- **Word Clouds** - Most common words associated with each animal
- **Sentiment Comparison** - Which animals are viewed most positively/negatively
- **Trends Over Time** - How sentiment changed across years
- **Heat Maps** - Sentiment intensity by year and animal
- **Distribution Charts** - Spread of sentiment scores

## Performance

### With GPU (RTX 4070, 3080, or similar):
- **500 articles**: ~1-2 minutes
- **1000 articles**: ~3-4 minutes
- **2000 articles**: ~6-8 minutes

### Without GPU (CPU only):
- **500 articles**: ~6-8 minutes
- **1000 articles**: ~12-15 minutes
- **2000 articles**: ~25-30 minutes

## Troubleshooting

### "GPU detected but not working properly"

**Fix:** Install Visual C++ Redistributables
1. Download: https://aka.ms/vs/17/release/vc_redist.x64.exe
2. Run as Administrator
3. Restart Jupyter kernel
4. Re-run Cell 1

### "API returned status code 502"

**Cause:** TROVE API server issues or invalid API key

**Fix:**
1. Check your API key is correct
2. Wait 5-10 minutes (TROVE may be down temporarily)
3. Try fewer articles per animal

### "HBoxModel errors" (widget warnings)

**Not a problem!** These are cosmetic warnings. GPU acceleration is still working.

**Optional fix:** Add to Cell 1:
```python
import os
os.environ['TRANSFORMERS_NO_ADVISORY_WARNINGS'] = '1'
```

### Running out of VRAM

**Fix:** Reduce batch size in Cell 1 by adding after GPU detection:
```python
BATCH_SIZE = 16  # Reduce from 24 to 16
```

## Tips for Best Results

### Article Count Recommendations:
- **Quick test**: 50-100 articles per animal (~5 minutes)
- **Standard analysis**: 200-500 articles per animal (~10-20 minutes)
- **Comprehensive**: 1000+ articles per animal (~30-60 minutes)

### Date Range Recommendations:
- **Narrow range** (10-20 years): More focused, faster
- **Wide range** (50+ years): Shows trends over time, slower

### Location Filtering:
- **All Australia**: Maximum articles, diverse perspectives
- **Specific states**: Regional differences in sentiment
- **Specific newspapers**: Consistent editorial voice

## Differences from Original Notebook

| Feature | Original | Streamlined |
|---------|----------|-------------|
| Package installation | Manual | Automatic (only if missing) |
| GPU setup | Verbose reporting | Silent (only reports problems) |
| User input | Edit code cells | Interactive prompts |
| Model selection | Multiple models | RoBERTa (best accuracy) |
| Complexity | Advanced users | Beginner-friendly |
| Outputs | Same | Same |

## Next Steps

After running the analysis:

1. **Open the HTML file** - Interactive charts show trends clearly
2. **Check the CSV files** - Raw data for further analysis
3. **Compare animals** - Look for surprising differences
4. **Analyze trends** - How did sentiment change over time?
5. **Share results** - Use the PNG files in presentations

## Need More Details?

See the full documentation in:
- **INSTALLATION.md** - Detailed installation instructions
- **MODEL_COMPARISON.md** - Understanding sentiment models
- **WINDOWS_GPU_FIX.md** - GPU troubleshooting for Windows

## Support

For issues or questions:
- Check the troubleshooting section above
- Review the full documentation files
- Ensure your TROVE API key is valid and active
