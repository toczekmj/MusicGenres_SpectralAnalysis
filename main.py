import PlaylistDownloder as pd
import SoundAnalyzer as sa
from mutagen.mp3 import MP3

genres = [
    "pop",
    "rock",
    "classical",
    "dance",
    "jazz"
]

if __name__ == '__main__':

    videos = pd.downloadPlaylist(
        "https://www.youtube.com/watch?v=ZY_2E8lVvFU&list=PL-KlXQk3aUpJZocck9etS5bhfIMZc8YZx&pp=gAQBiAQB"
        ,
        genres[0]
        ,
        append=False
    )

    for file in videos:
        sa.analyzeSample(file)