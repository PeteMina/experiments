#!/usr/bin/env python3
"""
Animal Sentiment Analysis - TROVE API
======================================

Analyzes emotional attitudes towards animal species in Australian newspapers
using the National Library of Australia's TROVE API.

Author: Pete Mina
License: MIT
"""

import requests
import json
import pandas as pd
import numpy as np
from pathlib import Path
import re
import time
from datetime import datetime
from collections import Counter

# NLP and Sentiment Analysis
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Visualization
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Download required NLTK data
def setup_nltk():
    """Download required NLTK datasets."""
    try:
        nltk.download('stopwords', quiet=True)
        nltk.download('punkt', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
        nltk.download('vader_lexicon', quiet=True)
        print("✓ NLTK data downloaded successfully")
    except Exception as e:
        print(f"Warning: Could not download NLTK data: {e}")


# Initialize sentiment analyzer
vader_analyzer = SentimentIntensityAnalyzer()


def query_trove_animal(animal, api_key, start_year, end_year, states=None,
                       article_types=None, max_results=500, min_relevance=5):
    """
    Query TROVE API for articles mentioning a specific animal.

    Args:
        animal: Animal species name to search for
        api_key: TROVE API key
        start_year: Starting year for search
        end_year: Ending year for search
        states: List of Australian states to filter by
        article_types: List of article types to filter by
        max_results: Maximum number of results to retrieve
        min_relevance: Minimum relevance score for filtering

    Returns:
        DataFrame containing article data
    """
    params = {
        'key': api_key,
        'zone': 'newspaper',
        'include': 'articleText',
        'n': 100,
        'encoding': 'json',
        'bulkHarvest': 'false',
        'reclevel': 'brief',
        'sortby': 'relevance'
    }

    if states:
        params['l-state'] = states
    if article_types:
        params['l-category'] = article_types

    params['q'] = f'{animal} date:[{start_year} TO {end_year}]'

    all_articles = []
    total_retrieved = 0

    print(f"Querying TROVE for '{animal}'...", end=" ", flush=True)

    response = requests.get('https://api.trove.nla.gov.au/v2/result', params=params)

    if response.status_code != 200:
        print(f"Error: API returned status code {response.status_code}")
        return pd.DataFrame()

    data = response.json()

    try:
        total_available = int(data['response']['zone'][0]['records']['total'])
        articles = data['response']['zone'][0]['records'].get('article', [])
    except (KeyError, IndexError):
        print("No results found.")
        return pd.DataFrame()

    all_articles.extend(articles)
    total_retrieved = len(articles)

    # Pagination
    while total_retrieved < min(max_results, total_available):
        params['s'] = f"*:{total_retrieved}"
        time.sleep(0.2)

        response = requests.get('https://api.trove.nla.gov.au/v2/result', params=params)
        if response.status_code != 200:
            break

        data = response.json()
        try:
            articles = data['response']['zone'][0]['records'].get('article', [])
            if not articles:
                break
            all_articles.extend(articles)
            total_retrieved += len(articles)
        except (KeyError, IndexError):
            break

    print(f"Retrieved {total_retrieved} articles (total available: {total_available})")

    if not all_articles:
        return pd.DataFrame()

    df = pd.json_normalize(all_articles)
    df['animal'] = animal

    # Process data
    if 'relevance.score' in df.columns:
        df['relevance'] = df['relevance.score'].astype('float')
        df = df[df['relevance'] >= min_relevance]

    if 'articleText' in df.columns:
        df['article_text'] = df['articleText'].str.replace(r'<[^<>]*>', '', regex=True)

    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month

    return df


def analyze_sentiment_textblob(text):
    """Analyze sentiment using TextBlob."""
    if pd.isna(text) or not text:
        return 0, 0
    try:
        blob = TextBlob(str(text))
        return blob.sentiment.polarity, blob.sentiment.subjectivity
    except:
        return 0, 0


def analyze_sentiment_vader(text):
    """Analyze sentiment using VADER."""
    if pd.isna(text) or not text:
        return {'neg': 0, 'neu': 0, 'pos': 0, 'compound': 0}
    try:
        return vader_analyzer.polarity_scores(str(text))
    except:
        return {'neg': 0, 'neu': 0, 'pos': 0, 'compound': 0}


def categorize_sentiment(score):
    """Categorize sentiment score."""
    if score > 0.1:
        return 'positive'
    elif score < -0.1:
        return 'negative'
    else:
        return 'neutral'


def add_sentiment_analysis(df):
    """Add sentiment analysis columns to dataframe."""
    if 'article_text' not in df.columns or df.empty:
        return df

    print("Analyzing sentiment...", flush=True)

    sentiments = df['article_text'].apply(analyze_sentiment_textblob)
    df['polarity'] = sentiments.apply(lambda x: x[0])
    df['subjectivity'] = sentiments.apply(lambda x: x[1])

    vader_scores = df['article_text'].apply(analyze_sentiment_vader)
    df['vader_negative'] = vader_scores.apply(lambda x: x['neg'])
    df['vader_neutral'] = vader_scores.apply(lambda x: x['neu'])
    df['vader_positive'] = vader_scores.apply(lambda x: x['pos'])
    df['vader_compound'] = vader_scores.apply(lambda x: x['compound'])

    df['sentiment_category'] = df['vader_compound'].apply(categorize_sentiment)

    print("✓ Sentiment analysis complete")
    return df


def create_wordcloud(text, title, output_path=None):
    """Create and save a word cloud."""
    if not text or pd.isna(text):
        print(f"No text available for {title}")
        return

    wc = WordCloud(
        width=1200, height=600, background_color='white',
        colormap='viridis', collocations=True,
        min_word_length=3, max_words=100
    )

    wc.generate(str(text))

    plt.figure(figsize=(15, 8))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, fontsize=16, fontweight='bold')
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✓ Saved word cloud to {output_path}")

    plt.close()


def plot_sentiment_over_time(df, output_dir=None):
    """Plot sentiment trends over time."""
    yearly_sentiment = df.groupby(['year', 'animal']).agg({
        'vader_compound': 'mean',
        'article_text': 'count'
    }).reset_index()
    yearly_sentiment.columns = ['year', 'animal', 'avg_sentiment', 'article_count']

    fig = px.line(
        yearly_sentiment, x='year', y='avg_sentiment', color='animal',
        title='Sentiment Trends Over Time',
        labels={'avg_sentiment': 'Average Sentiment Score', 'year': 'Year'},
        markers=True, hover_data=['article_count']
    )

    fig.add_hline(y=0, line_dash="dash", line_color="gray")
    fig.update_layout(height=600)

    if output_dir:
        output_path = Path(output_dir) / "sentiment_trends.html"
        fig.write_html(str(output_path))
        print(f"✓ Saved sentiment trends to {output_path}")

    return fig


def create_sentiment_heatmap(df, output_dir=None):
    """Create sentiment heatmap by animal and state."""
    if 'state' not in df.columns:
        print("No state information available for heatmap")
        return None

    heatmap_data = df.groupby(['animal', 'state'])['vader_compound'].mean().reset_index()
    heatmap_pivot = heatmap_data.pivot(index='animal', columns='state', values='vader_compound')

    plt.figure(figsize=(14, 8))
    sns.heatmap(heatmap_pivot, annot=True, fmt='.3f', cmap='RdYlGn',
                center=0, cbar_kws={'label': 'Average Sentiment'}, linewidths=0.5)
    plt.title('Sentiment Heatmap by Animal and State', fontsize=16, fontweight='bold')
    plt.xlabel('State', fontsize=12)
    plt.ylabel('Animal', fontsize=12)
    plt.tight_layout()

    if output_dir:
        output_path = Path(output_dir) / "sentiment_heatmap.png"
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✓ Saved heatmap to {output_path}")

    plt.close()


def save_results(df, output_dir, start_year, end_year):
    """Save analysis results to CSV files."""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Save complete dataset
    main_file = output_path / f"all_animals_sentiment_{start_year}_{end_year}.csv"
    df.to_csv(main_file, index=False)
    print(f"✓ Saved complete dataset to {main_file}")

    # Save individual animal files
    for animal in df['animal'].unique():
        animal_df = df[df['animal'] == animal]
        animal_file = output_path / f"{animal}_sentiment_{start_year}_{end_year}.csv"
        animal_df.to_csv(animal_file, index=False)

    # Save summary statistics
    summary = df.groupby('animal').agg({
        'vader_compound': ['mean', 'std', 'min', 'max'],
        'polarity': ['mean', 'std'],
        'article_text': 'count'
    }).round(4)
    summary.columns = ['_'.join(col).strip() for col in summary.columns.values]

    summary_file = output_path / f"summary_statistics_{start_year}_{end_year}.csv"
    summary.to_csv(summary_file)
    print(f"✓ Saved summary statistics to {summary_file}")

    return output_path


def main():
    """Main execution function."""
    print("\n" + "="*60)
    print("Animal Sentiment Analysis - TROVE API")
    print("="*60 + "\n")

    # Setup
    setup_nltk()

    # Configuration
    API_KEY = input("Enter your TROVE API key: ").strip()

    if not API_KEY:
        print("Error: API key is required!")
        return

    # Default configuration
    animals = ['kangaroo', 'koala', 'dingo', 'platypus', 'wombat',
               'crocodile', 'snake', 'shark']
    start_year = 1900
    end_year = 1950
    max_articles = 500
    min_relevance = 5

    print(f"\nAnalyzing {len(animals)} animals from {start_year} to {end_year}")
    print(f"Animals: {', '.join(animals)}\n")

    # Collect data
    print("="*60)
    print("COLLECTING DATA FROM TROVE")
    print("="*60 + "\n")

    all_data = []
    for animal in animals:
        df = query_trove_animal(
            animal, API_KEY, start_year, end_year,
            max_results=max_articles, min_relevance=min_relevance
        )
        if not df.empty:
            all_data.append(df)
        time.sleep(0.5)

    if not all_data:
        print("No data collected. Exiting.")
        return

    df_combined = pd.concat(all_data, ignore_index=True)
    print(f"\n✓ Total articles collected: {len(df_combined)}\n")

    # Analyze sentiment
    print("="*60)
    print("PERFORMING SENTIMENT ANALYSIS")
    print("="*60 + "\n")

    df_combined = add_sentiment_analysis(df_combined)

    # Print summary
    print("\n" + "="*60)
    print("SENTIMENT SUMMARY")
    print("="*60 + "\n")

    print("Average sentiment by animal:")
    sentiment_summary = df_combined.groupby('animal')['vader_compound'].mean().sort_values(ascending=False)
    for animal, score in sentiment_summary.items():
        sentiment = "POSITIVE" if score > 0.1 else "NEGATIVE" if score < -0.1 else "NEUTRAL"
        print(f"  {animal.capitalize():15s}: {score:+.3f} ({sentiment})")

    # Save results
    print("\n" + "="*60)
    print("SAVING RESULTS")
    print("="*60 + "\n")

    output_dir = f"animal_sentiment_{start_year}_{end_year}"
    save_results(df_combined, output_dir, start_year, end_year)

    # Generate visualizations
    print("\n" + "="*60)
    print("GENERATING VISUALIZATIONS")
    print("="*60 + "\n")

    # Word clouds
    for animal in animals:
        animal_text = ' '.join(
            df_combined[df_combined['animal'] == animal]['article_text'].dropna()
        )
        if animal_text:
            output_path = Path(output_dir) / f"wordcloud_{animal}.png"
            create_wordcloud(animal_text, f"Word Cloud - {animal.title()}", output_path)

    # Sentiment trends
    plot_sentiment_over_time(df_combined, output_dir)

    # Heatmap
    create_sentiment_heatmap(df_combined, output_dir)

    print("\n" + "="*60)
    print("ANALYSIS COMPLETE!")
    print("="*60)
    print(f"\nAll results saved to: {output_dir}/")
    print("\nGenerated files:")
    print("  - CSV files with complete data and analysis")
    print("  - Word clouds for each animal")
    print("  - Sentiment trend graphs")
    print("  - Sentiment heatmaps")
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
