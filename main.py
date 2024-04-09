import librosa

import Libraries.PlaylistDownloder
from Libraries import SoundAnalyzer as sa

genres = [
    "pop",
    "rock",
    "classical",
    "dance",
    "jazz"
]

if __name__ == '__main__':
    # path = Libraries.PlaylistDownloder.downloadMp3("https://www.youtube.com/watch?v=Rgrm-CCgDxc", "notes_no_bitrate")
    path = Libraries.PlaylistDownloder.downloadMp3("https://www.youtube.com/watch?v=wfF0zHeU3Zs", "classical")
    music, sr = librosa.load(path)
    sa.plot_magnitude_spectrum(music, path, sr)
