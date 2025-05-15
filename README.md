# Song Recommendation Generator
**Enjoying Music, Made Easier**

### A command-line tool (CLI) that generates a list of 20 songs similar to a user-inputted track, using audio features and cosine similarity, via tracks on a static dataset accessed by the Spotify API.

*To view the dataset used in this project, click [here](https://www.kaggle.com/datasets/priyamchoksi/spotify-dataset-114k-songs).*

*To view the Spotify API documentation for the audio features used in this project, click [here](https://developer.spotify.com/documentation/web-api/reference/get-audio-features).*

### Features

1. Content-based recommendation: locates tracks with similar audio characteristics.
2. Accepts user input by track name and artist.
3. Returns top 20 recommendations with similarity percentages.
4. Optional: save recommendations to a CSV.

### Project Structure

    Song-Recommendation-Generator/

    ├── main.ipynb                   Data Analysis file

    ├── mood_playlist_generator.py   Model function -> generates top 20 songs

    ├── playlist_cli.py              CLI interface script for UX

    ├── dataset.csv                  Spotify Dataset used Cleaned dataset of tracks

    ├── README.md                    Project overview

    └── requirements.txt             Python dependencies

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/JamieBennett-Dev/Mood-Playlist-Generator
    cd Mood-Playlist-Generator
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Prepare the data**: Ensure `dataset.csv` is in the project directory. This should contain at least the following columns:
    - `track_id`.
    - `track_name`.
    - `artists`.
    - `track_genre`.
    - Audio feature columns: `danceability`, `energy`, `key`, `loudness`, `mode`, `speechiness`, `acousticness`, `instrumentalness`, `liveness`, `valence`, `tempo`.

2. **Run the CLI**
    ```bash
    python playlist_cli.py
    ```

3. **Follow prompts**:
    - Enter a song title and artist name (e.g., "Rotten Apple", "Alice In Chains")

4. **View recommendations**: The script prints the top 20 similar songs along with similarity scores.

5. **Save to CSV (optional)**: After recommendations are displayed, choose `Y` to save them to `recommendations.csv`.
