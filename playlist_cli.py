# playlist_cli.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from mood_playlist_generator import generate_mood_playlist

def load_data():
    
    df = pd.read_csv('dataset.csv')  
    
    df = df.drop_duplicates(subset=['track_id'])

    features = [
        'danceability', 'energy', 'key', 'loudness', 'mode',
        'speechiness', 'acousticness', 'instrumentalness',
        'liveness', 'valence', 'tempo'
    ]

    scaler = StandardScaler()
    X = scaler.fit_transform(df[features])

    return df, X

def main():
    print("Welcome to the Mood Playlist Generator!\n")

    df, features_scaled = load_data()

    song_title = input("Enter the song title: ")
    artist_name = input("Enter the artist name: ")

    try:
        recs = generate_mood_playlist(
            df=df,
            features_scaled=features_scaled,
            track_name=song_title,
            artist=artist_name,
            top_n=20
        )
        print("\nHere are your top 20 mood-matched tracks:\n")
        print(recs[['track_name','artist(s)','similarity']].to_string(index=False))
        
        while True:
            save = input("\nWould you like to save these to a CSV file? (Y/N): ").strip().lower()
            if save in ('y', 'n'):
                break
            print("❌ Invalid input! Please enter 'Y' or 'N'.")

        if save == 'y':
            output_path = 'recommendations.csv'
            recs.to_csv(output_path, index=False)
            print(f"✅ Saved recommendations to {output_path}")
        else:
            print("Okay, not saving to CSV.")

        
        
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
