# all code belov was generated using ChatGPT
# only in test purposes
# please keep that in mind
import os
import shutil

import joblib
import librosa
import numpy as np
from pydub import AudioSegment
from pytube import YouTube
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model


def convertStreamToMp3(file):
    print(f'Converting {file} to mp3')
    original_extension = file.split('.')[-1]
    mp3_converted_file = AudioSegment.from_file(file, original_extension)
    new_path = file[:-3] + 'mp3'
    mp3_converted_file.export(new_path, format='mp3')
    os.remove(file)


def downloadMp3(url, music_dir, append=True):
    video = YouTube(url)

    if os.path.isdir(music_dir) and not append:
        shutil.rmtree(music_dir)

    if not append:
        os.mkdir(music_dir)

    stream = video.streams.filter(only_audio=True).first()
    name = f'{stream.title}.mp4'

    print(f'Downloading {name}')
    stream.download(output_path=music_dir, filename=name)
    file = os.path.join(music_dir, name)
    convertStreamToMp3(file)
    return file.replace('.mp4', '.mp3')


model_path = '../music_genre_model.keras'
scaler_path = '../scaler.pkl'
csv_path = '../music_features.csv'
test_path = '../test_data'
downloads = '../downloads'


model = load_model(model_path)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
scaler = joblib.load(scaler_path)


def extract_features(track_path):
    y, sr = librosa.load(track_path)  # ograniczenie do 30 sekund
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


def predict_genre(track_path):
    features = extract_features(track_path)
    features = np.array(features).reshape(1, -1)
    features = scaler.transform(features)
    prediction = model.predict(features)
    genre = encoder.inverse_transform([np.argmax(prediction)])
    return genre[0]


import pandas as pd
data = pd.read_csv(csv_path)
y = data['genre']
encoder = LabelEncoder()
encoder.fit(y)


url = ""
urls = []

while url != 'end':
    current = input()
    if current == 'end':
        break
    urls.append(current)

for u in urls:
    downloadMp3(u, downloads)


files_list = os.listdir(downloads)
results = []
for filename in files_list:
    if filename.endswith('.mp3'):
        currentpath = os.path.join(downloads, filename)
        result = predict_genre(currentpath)
        results.append(f'{filename} -> {result}\n')
file = open('predicted.txt', 'w')
file.writelines(results)
file.close()




