import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def song_recommendation_generator(df, features_scaled, track_id=None, track_name=None, artist=None, top_n=20):
    """
    Function that returns the top N similar songs based on the input.
    
    Parameters:
    - df: DataFrame containing song data (track_name, artist(s), track_id, etc.).
    - features_scaled: Scaled feature matrix for the songs.
    - track_id: Optional track ID to search for.
    - track_name: Optional track name to search for.
    - artist: Optional artist name to search for.
    - top_n: The number of similar tracks to return. Default is 20.
    
    Returns:
    - DataFrame with the top N similar tracks.
    """
    
    if track_id:
        match = df[df['track_id'] == track_id]
    elif track_name and artist:
        match = df[(df['track_name'].str.lower() == track_name.lower()) & 
                   (df['artists'].str.lower().str.contains(artist.lower()))]
    else:
        raise ValueError("Provide either a track_id or both track_name and artist.")

    if match.empty:
        raise ValueError("Song not found. Check the spelling or availability.")

    idx = match.index[0]

    sim_scores = cosine_similarity([features_scaled[idx]], features_scaled)[0]

    sim_df = pd.DataFrame({
        'track_name': df['track_name'],
        'artist(s)': df['artists'],
        'track_id': df['track_id'],
        'track_genre': df['track_genre'],
        'similarity': np.round(sim_scores, 2)
    })
    
    sim_df['similarity'] = (sim_df['similarity'] * 100).round().astype(int).astype(str) + '%'

    sim_df = sim_df[sim_df['track_id'] != df.loc[idx, 'track_id']]
    
    recommended = sim_df.sort_values(by='similarity', ascending=False).head(top_n)

    return recommended
