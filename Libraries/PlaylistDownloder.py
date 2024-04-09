import shutil
import os
from pytube import Playlist
from pytube import YouTube
from pydub import AudioSegment


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


def downloadPlaylist(url, music_dir, append=True):
    playlist = Playlist(url)

    if os.path.isdir(music_dir) and not append:
        shutil.rmtree(music_dir)

    if not append:
        os.mkdir(music_dir)

    i = 0
    names = []

    for video in playlist.videos:
        stream = video.streams.filter(only_audio=True).first()
        name = f'{i}.mp4'
        i += 1

        while os.path.isfile(os.path.join(music_dir, name)):
            i += 1
            name = f'{i}.mp4'

        print(f'Downloading {name}')
        stream.download(output_path=music_dir, filename=name)
        names.append(
            os.path.join(music_dir, name.replace('.mp4', '.mp3'))
        )
        convertStreamToMp3(os.path.join(music_dir, name))
    return names