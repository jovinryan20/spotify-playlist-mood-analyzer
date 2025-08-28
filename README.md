# 🎵 Spotify Playlist Mood Analyzer

A data science project that connects to Spotify using the **Spotify Web API** and analyzes the mood of songs in a playlist using their audio features. The project also visualizes the distribution of moods.

---

## 🚀 Features
- Connects to Spotify using your account credentials
- Fetches songs from any public Spotify playlist
- Extracts **audio features** like danceability, energy, tempo, etc.
- Classifies songs into moods (Happy, Sad, Energetic, Calm)
- Visualizes results with **matplotlib** and **seaborn**
- Can be easily customized for your own playlists

---

## 📂 Project Structure
spotify-playlist-mood-analyzer/

│-- app.py # Main Python script

│-- requirements.txt # Dependencies

│-- README.md # Project documentation

│-- .env # Stores Spotify API credentials (not uploaded to GitHub)

---

## 🛠 Installation & Setup

### 1️⃣ Clone the repository

git clone https://github.com/YOUR_USERNAME/spotify-playlist-mood-analyzer.git
cd spotify-playlist-mood-analyzer

2️⃣ Install dependencies: 
pip install -r requirements.txt

3️⃣ Set up Spotify API

Go to Spotify Developer Dashboard

Create a new application

Get your Client ID and Client Secret

Create a .env file in the project root with:

SPOTIPY_CLIENT_ID=your_client_id

SPOTIPY_CLIENT_SECRET=your_client_secret

SPOTIPY_REDIRECT_URI=http://127.0.0.1:9090

4️⃣ Run the project: (python)

app.py

📊 Example Output: 

A bar chart showing mood distribution of songs

Playlist data with mood classification in a Pandas DataFrame

🎯 Future Enhancements: 

Add sentiment analysis using lyrics

Build a web dashboard for interactive mood analysis

Auto-create mood-based playlists on Spotify

👨‍💻 Author

Created by Jovin Ryan Samuel ✨

If you like this project, ⭐ the repo on GitHub!
