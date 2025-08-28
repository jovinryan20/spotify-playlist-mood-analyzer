import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("spotify_songs.csv")

# Select important columns
mood_df = df[['track_name', 'artist_name', 'danceability', 'energy', 'valence', 'tempo']]

# Simulate a "playlist"
playlist_df = mood_df.sample(10, random_state=42).reset_index(drop=True)

# Mood analysis function
def mood_label(row):
    if row['valence'] > 0.6 and row['energy'] > 0.6:
        return "Happy/Energetic"
    elif row['valence'] > 0.6:
        return "Happy/Calm"
    elif row['valence'] < 0.4 and row['energy'] > 0.6:
        return "Angry/Energetic"
    elif row['valence'] < 0.4:
        return "Sad/Calm"
    else:
        return "Neutral"

playlist_df['Mood'] = playlist_df.apply(mood_label, axis=1)

# Print playlist with moods
print("Your Playlist with Mood Labels:\n")
print(playlist_df[['track_name', 'artist_name', 'Mood']])

# Visualization
plt.figure(figsize=(8,5))
sns.countplot(x='Mood', data=playlist_df, hue='Mood', palette='Set2', dodge=False, legend=False)
plt.title("Playlist Mood Distribution")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("plots/mood_distribution.png")  
plt.show()
