# all code belov was generated using ChatGPT
# only in test purposes
# please keep that in mind
import csv
import os

import librosa
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential

data_path = ''
model_path = ''
# genres = ['CLASSICAL', 'COUNTRY', 'HIPHOP', 'POP', 'JAZZ', 'RAP']
genres = ['CLASSICAL']


def extract_features(track_path):
    y, sr = librosa.load(track_path, duration=1)  # ograniczenie do 30 sekund
    features = []
    spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)
    features.append(np.mean(spectral_centroids))
    spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    features.append(np.mean(spectral_rolloff))
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y)
    features.append(np.mean(zero_crossing_rate))
    mfccs = librosa.feature.mfcc(y=y, sr=sr)
    for mfcc in mfccs:
        features.append(np.mean(mfcc))
    return features


header = ['genre', 'spectral_centroid', 'spectral_rolloff', 'zero_crossing_rate'] + [f'mfcc_{i}' for i in range(22050)]
data = []

for genre in genres:
    genre_path = os.path.join(data_path, genre)
    list_of_files = os.listdir(genre_path)
    number_of_files = len(list_of_files)
    counter = 1
    for file_name in list_of_files:
        print(f'{counter} / {number_of_files}: {file_name}')
        counter += 1
        if file_name.endswith('.mp3'):
            track_path = os.path.join(genre_path, file_name)
            features = extract_features(track_path)
            data.append([genre] + features)

csv_path = os.path.join(model_path, 'music_features.csv')
with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

data = pd.read_csv(csv_path)
X = data.drop('genre', axis=1)
y = data['genre']
encoder = LabelEncoder()
y = encoder.fit_transform(y)
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential([
    Dense(256, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.5),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(6, activation='softmax')  # 6 music genres
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(X_train, y_train, epochs=500, validation_data=(X_test, y_test))

test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Test accuracy: {test_acc}')

model_file_path = os.path.join(model_path, 'music_genre_model.keras')
model.save(model_file_path)

import joblib

scaler_path = os.path.join(model_path, 'scaler.pkl')
joblib.dump(scaler, scaler_path)
