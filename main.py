from Libraries import FftPreparation as fp
from Libraries import SoundAnalyzer as sa

CHUNK = 2000

if __name__ == '__main__':
    path = "/Users/toczekmj/PycharmProjects/spectralAnalysis/metal/Koń na Białym Rycerzu.mp3"

    signal, sample_rate = sa.load_song(path)
    x_mean, y_mean, beans = fp.matrix_average(signal, sample_rate, CHUNK=CHUNK, offset_hz=0)
    sa.plot_frequency_graph_semilog(y_mean, x_mean, beans=CHUNK, offset_hz=0)
    sa.plot_frequency_graph(y_mean, x_mean, beans=CHUNK, offset_hz=0)

