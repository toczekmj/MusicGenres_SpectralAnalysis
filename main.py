import getopt
import os.path
import shutil
import sys
from glob import glob

import numpy as np

from Libraries.CvsExport import export_data_to_csv as export_csv
from Libraries.FftPreparation import matrix_average
from Libraries.PlaylistDownloder import downloadPlaylist, downloadMp3
from Libraries.SoundAnalyzer import load_song

CHUNK = 3000


def get_song_frequency(file_path: str, offset_hz: int = 0):
    signal, sample_rate = load_song(file_path)
    x_mean, y_mean, beans = matrix_average(signal, sample_rate, CHUNK=CHUNK, offset_hz=offset_hz)
    return x_mean, y_mean, beans


def average_from_genre(direcotry_path: str, offset_hz: int = 0):
    base_path = os.path.basename(direcotry_path)
    songs = glob(base_path + '/*.mp3')
    x = []
    y = []
    b = []

    for song in songs:
        freq, magnitude, beans = get_song_frequency(song, offset_hz=offset_hz)
        x.append(freq)
        y.append(magnitude)
        b.append(beans)

    freq_matrix = np.matrix(x)
    magnitude_matrix = np.matrix(y)
    beans_matrix = np.matrix(b)

    freq_mean = np.squeeze(np.asarray(freq_matrix.mean(0)))
    magnitude_matrix = np.squeeze(np.asarray(magnitude_matrix.mean(0)))
    beans_mean = np.squeeze(np.asarray(beans_matrix.mean(0)))
    return list(freq_mean), list(magnitude_matrix), list(beans_mean)


def downloadSongs(genre_name: str, download_link: str, is_playlist: bool, delete_if_exists: bool):
    if download_link == "":
        print("Download URL cannot be empty")
        sys.exit(2)

    if os.path.isdir(genre_name + "_CSV"):
        if delete_if_exists:
            shutil.rmtree(genre_name + "_CSV")
            os.mkdir(genre_name + "_CSV")
    else:
        os.mkdir(genre_name + "_CSV")

    if is_playlist:
        downloadPlaylist(download_link, genre_name, append=delete_if_exists)
    else:
        downloadMp3(download_link, genre_name, append=delete_if_exists)


def calculate(genre_name: str):
    files = glob(genre_name+'/*.mp3')

    if os.path.isdir(genre_name + "_CSV"):
        if delete_if_exists:
            shutil.rmtree(genre_name + "_CSV")
            os.mkdir(genre_name + "_CSV")
    else:
        os.mkdir(genre_name + "_CSV")

    for song in files:
        current_path = song
        csv_path = current_path.replace(f'{genre_name}\\', f'{genre_name}_CSV\\')
        print(song)
        x, y, b = get_song_frequency(current_path)
        export_csv(x, y, genre_name, csv_path, False)



if __name__ == '__main__':
    # calculate_real_time("EXPORT")
    genre_name = ""
    download_link = ""
    is_playlist = False
    delete_if_exists = False
    analyze_only = False

    arguments = sys.argv[1:]
    try:
        opts, args = getopt.getopt(arguments, "hg:u:pda")
    except getopt.GetoptError:
        print(
            'main.py -g | --genre <genre_name> \n-u | --url <youtube url> \n-p | --playlist if it is not a single clip, but playlist '
            '\n -d | --delete if there alreaddy exists folder with such genre name it will delete it before downloading, otherwise append '
            '\n')
        sys.exit(2)

    for option, arg in opts:
        if option in ('-h' '--help'):
            print('main.py -g | --genre <genre_name> \n-u | --url <youtube url> \n-p | --playlist if it is not a single clip, but playlist '
                  '\n-d | --delete if there already exists folder with such genre name it will delete it before downloading, otherwise append '
                  '\na')
        elif option in ('-g', '--genre'):
            genre_name = arg
        elif option in ('-u', '--url'):
            download_link = arg
        elif option in ('-p', '--playlist'):
            is_playlist = True
        elif option in ('-d', '--delete'):
            delete_if_exists = True
        elif option in ('-a', '--analyze'):
            analyze_only = True

    if genre_name == "":
        print("Genre name cannot be empty. --help or -h for help")
        sys.exit(2)

    if analyze_only:
        calculate(genre_name)
        sys.exit(0)

    if download_link == "":
        print("Not downloading anything. We will work on already downloaded songs.")
    else:
        downloadSongs(genre_name, download_link, is_playlist, delete_if_exists)

    calculate(genre_name)

