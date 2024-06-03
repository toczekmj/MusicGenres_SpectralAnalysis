from glob import glob

from Libraries.CvsExport import export_data_to_csv as export_csv
from Libraries.SoundAnalyzer import calculate_magnitude_spectrum, load_song

if __name__ == '__main__':
    path = ''

    files = glob(path + '/*.mp3')

    for song in files:
        print(song)
        signal, sample_rate = load_song(song)
        y, x = calculate_magnitude_spectrum(signal, sample_rate)
        export_path = ""
        export_csv(x, y, "export", export_path, False)