import glob
from Libraries import SoundAnalyzer as sa

genres = [
    "pop",
    "rock",
    "classical",
    "dance",
    "jazz",
    "country"
]

if __name__ == '__main__':
    dir_path = f"/Users/toczekmj/PycharmProjects/spectralAnalysis/{genres[0]}/*"
    files = glob.glob(dir_path)
    charts = []

    for file in files:
        signal, rate = sa.load_song(file)
        mg, freq, beans = sa.calculate_magnitude_spectrum(signal, rate, 200)
        sa.plot_frequency_graph(mg, freq, beans, 200)
