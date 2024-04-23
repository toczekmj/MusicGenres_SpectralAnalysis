from Libraries import FftPreparation as fp
from Libraries import SoundAnalyzer as sa
from Libraries import GraphPloter as gp

CHUNK = 3000


def get_song_frequency(file_path: str, offset_hz: int = 0):
    signal, sample_rate = sa.load_song(file_path)
    x_mean, y_mean, beans = fp.matrix_average(signal, sample_rate, CHUNK=CHUNK, offset_hz=offset_hz)
    return x_mean, y_mean, beans


if __name__ == '__main__':
    path = "/Users/toczekmj/PycharmProjects/spectralAnalysis/metal/Koń na Białym Rycerzu.mp3"

    x_mean, y_mean, beans = get_song_frequency(path)
    gp.plot_frequency_graph_semilog(x_mean, y_mean, beans=beans, offset_hz=0)
    gp.plot_frequency_graph(x_mean, y_mean, beans=beans, offset_hz=0)

