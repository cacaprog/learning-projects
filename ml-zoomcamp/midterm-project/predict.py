from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model and the scaler
with open('rf_model.bin', 'rb') as f_in_model, open('scaler.pkl', 'rb') as f_in_scaler:
    dv, model = pickle.load(f_in_model)
    scaler = pickle.load(f_in_scaler)

@app.route('/predict', methods=['POST'])
def predict():
    track_features = request.json
    
    # Preprocess features
    track_features['loudness'] = scaler.transform([[track_features['loudness']]])[0][0]
    
    # Ensure all required features are present and in the correct order
    model_columns = [
        'track_popularity',
        'playlist_genre',
        'playlist_subgenre',
        'acousticness',
        'danceability',
        'duration_ms',
        'energy',
        'instrumentalness',
        'key',
        'liveness',
        'loudness',
        'mode',
        'speechiness',
        'tempo'
    ]
    
    # Extract features in the correct order, filling missing values with 0
    X = dv.transform([{col: track_features.get(col, 0) for col in model_columns}])
    
    # Predict
    y_pred = model.predict(X)[0]
    
    # Return the result
    result = {
        'valence_prediction': y_pred,
        'message': 'Awesome, play it!' if y_pred >= 0.65 else 'Choose another track'
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
