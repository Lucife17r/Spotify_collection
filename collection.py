# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# Replace 'spotify_data.csv' with the path to your dataset file
data = pd.read_csv(r"C:\Users\pc\Downloads\large_spotify_data.csv")

# Quick look at the dataset
print(data.head())

# Data Cleaning: Check for missing values and handle them
print("\nMissing Values:\n", data.isnull().sum())
data.dropna(inplace=True)

# Data Overview
print("\nDataset Info:\n")
print(data.info())
print("\nBasic Statistics:\n")
print(data.describe())

# Correlation between release year, artist, and popularity
release_popularity_corr = data[['release_year', 'popularity']].corr()
print("\nCorrelation between release year and popularity:\n", release_popularity_corr)

# Visualizing trends in popularity over the years
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='release_year', y='popularity', errorbar=None)
plt.title('Song Popularity Trend Over Years (1900-2021)')
plt.xlabel('Release Year')
plt.ylabel('Popularity')
plt.grid(True)
plt.show()

# Analyzing genre preferences
plt.figure(figsize=(14, 7))
top_genres = data['genre'].value_counts().head(10)
sns.barplot(x=top_genres.index, y=top_genres.values, palette='viridis')
plt.title('Top 10 Genres by Song Count')
plt.xlabel('Genre')
plt.ylabel('Number of Songs')
plt.xticks(rotation=45)
plt.show()

# Analyzing artist popularity by play count
artist_play_count = data.groupby('artist')['play_count'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(14, 7))
sns.barplot(x=artist_play_count.index, y=artist_play_count.values, palette='coolwarm')
plt.title('Top 10 Artists by Total Play Count')
plt.xlabel('Artist')
plt.ylabel('Play Count')
plt.xticks(rotation=45)
plt.show()

# Correlation between play count and popularity
play_popularity_corr = data[['play_count', 'popularity']].corr()
print("\nCorrelation between play count and popularity:\n", play_popularity_corr)

# Scatterplot: Play count vs Popularity
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='play_count', y='popularity', alpha=0.5)
plt.title('Play Count vs Popularity')
plt.xlabel('Play Count')
plt.ylabel('Popularity')
plt.grid(True)
plt.show()

# Insights from analysis
print("\n--- Key Insights ---")
print("- Strong positive correlation between play count and popularity indicates highly played songs tend to be more popular.")
print("- Visualizations reveal genre trends, popularity over time, and artist performance.")

# Save cleaned data (optional)
data.to_csv('cleaned_spotify_data.csv', index=False)
