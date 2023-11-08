import requests

# Sample data for prediction
track_features = {
    'track_popularity': 70,
    'playlist_genre': "pop",
    'playlist_subgenre': "dance pop",
    'acousticness': 0.1,
    'danceability': 0.8,
    'duration_ms': 210000,
    'energy': 0.9,
    'instrumentalness': 0.0,
    'key': 5,
    'liveness': 0.2,
    # Normally we would scale 'loudness' using the MinMaxScaler fitted on the training data
    'loudness': -5.0,  # Placeholder value, should be scaled
    'mode': 1,
    'speechiness': 0.05,
    'tempo': 120.0
}

# URL of the Flask app predict route
url = 'http://127.0.0.1:5000/predict'

# Make the POST request
response = requests.post(url, json=track_features)

# Print the response
print(response.json())