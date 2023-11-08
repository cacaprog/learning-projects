#!/usr/bin/env python
# coding: utf-8

# Import libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import pickle

# Parameters
output_model_file = 'rf_model.bin'
output_scaler_file = 'scaler.pkl'

# Data preparation
df = pd.read_csv('spotify_songs.csv')
df = df.drop(columns='track_album_release_date')
df = df.dropna(subset=['track_album_name', 'track_artist', 'track_name'])
df = df.drop_duplicates(subset='track_id', keep='first')

scaler = MinMaxScaler()
feature_scaled = ['loudness']
df['loudness'] = scaler.fit_transform(df[feature_scaled].values.reshape(-1, 1))

# Split the dataset
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
    'tempo',
    'valence'  # Assuming 'valence' should be included here and dropped later
]

df = df[model_columns]
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=42)

# Reset indices
df_full_train = df_full_train.reset_index(drop=True)
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

# Extract target variable 'valence'
y_full_train = df_full_train.pop('valence').values
y_train = df_train.pop('valence').values
y_val = df_val.pop('valence').values
y_test = df_test.pop('valence').values

# Training function
def train(df_train, y_train):
    dicts = df_train.to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = RandomForestRegressor(n_estimators=61,
                                  max_depth=20,
                                  min_samples_leaf=3,
                                  criterion='squared_error',
                                  random_state=42)
    model.fit(X_train, y_train)
    return dv, model

# Prediction and evaluation function
def predict_and_evaluate(df, dv, model, y_true):
    dicts = df.to_dict(orient='records')
    X = dv.transform(dicts)
    y_pred = model.predict(X)
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    return y_pred, rmse

# Validation
print('Doing validation...')
dv, model = train(df_train, y_train)
_, rmse = predict_and_evaluate(df_val, dv, model, y_val)
print(f'RMSE of validation: {rmse}')

# Training the final model
print('Training the final model...')
dv, model = train(df_full_train, y_full_train)
_, rmse = predict_and_evaluate(df_test, dv, model, y_test)
print(f'RMSE of test: {rmse}')

# Save the model and the scaler
try:
    with open(output_model_file, 'wb') as f_out_model, open(output_scaler_file, 'wb') as f_out_scaler:
        pickle.dump((dv, model), f_out_model)
        pickle.dump(scaler, f_out_scaler)
    print(f'The model is saved to {output_model_file} and the scaler to {output_scaler_file}')
except Exception as e:
    print(f'Error saving the model or scaler: {e}')
