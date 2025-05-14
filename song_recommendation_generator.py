## playlist generator script
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def song_recommendation_generator(df, features_scaled, track_name=None, artist=None, top_n=20):
    
    if track_name and artist:
        match = df[(df['track_name'].str.lower() == track_name.lower()) & 
                   (df['artists'].str.lower().str.contains(artist.lower()))]
    else:
        raise ValueError("Provide a track_name and artist.")

    if match.empty:
        raise ValueError("Song not found. Check the spelling or availability.")

    idx = match.index[0]

    sim_scores = cosine_similarity([features_scaled[idx]], features_scaled)[0]

    sim_df = pd.DataFrame({
        'track_name': df['track_name'],
        'artist(s)': df['artists'],
        'track_genre': df['track_genre'],
        'similarity': np.round(sim_scores, 2)
    })
    
    sim_df = sim_df.drop_duplicates(subset=['track_name', 'artist(s)'])
    
    sim_df['similarity'] = (sim_df['similarity'] * 100).round().astype(int).astype(str) + '%'
    
    recommended = sim_df.sort_values(by='similarity', ascending=False).head(top_n)

    return recommended
