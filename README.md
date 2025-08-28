# Spotify Playlist Mood Analyzer

## Overview
This project analyzes the **mood of a Spotify playlist** using real audio features like danceability, energy, valence, and tempo. The goal is to categorize each track into moods such as Happy/Energetic, Sad/Calm, or Neutral and visualize the overall playlist mood distribution.

## Dataset
The project uses a **Spotify songs dataset** from Kaggle:
[Ultimate Spotify Tracks DB](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)

- `track_name`
- `artist_name`
- `danceability`
- `energy`
- `valence`
- `tempo`

## Features
- Assigns a **mood label** to each song based on valence and energy.
- Visualizes **mood distribution** using a bar chart.
- Fully reproducible without Spotify API (avoids 403 errors).

## How to Run
1. Clone this repository
2. Install required libraries:
    pip install -r requirements.txt
3. Run the app:
python app.py
4. A bar chart will appear showing the playlist mood distribution.

## Example Output

Track Name Artist Name Mood

Song 1 Artist A Happy/Energetic
Song 2 Artist B Sad/Calm
...

A bar chart is also generated and saved in `plots/mood_distribution.png`.
