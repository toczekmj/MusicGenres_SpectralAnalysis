import librosa
import glob

import Libraries.PlaylistDownloder
from Libraries import SoundAnalyzer as sa
from matplotlib import pyplot as plt

genres = [
    "pop",
    "rock",
    "classical",
    "dance",
    "jazz",
    "country"
]

if __name__ == '__main__':
    # path = Libraries.PlaylistDownloder.downloadMp3("https://www.youtube.com/watch?v=Rgrm-CCgDxc", f'{genres[5]}')
    dirpath = f"/Users/toczekmj/PycharmProjects/spectralAnalysis/{genres[5]}/*"
    files = glob.glob(dirpath)
    charts = []

    for file in files:
        music, sr = librosa.load(file)
        charts.append(sa.np_plot_magnitude_spectrum(music, file, sr))
    plt.show()
