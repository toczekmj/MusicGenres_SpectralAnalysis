from Libraries import FftPreparation as fp
from Libraries import SoundAnalyzer as sa

CHUNK = 500

if __name__ == '__main__':
    path = '/Users/toczekmj/PycharmProjects/spectralAnalysis/pop/One More Night.mp3'

    signal, sample_rate = sa.load_song(path)
    x_mean, y_mean, beans = fp.prepare_matrix(signal, sample_rate, CHUNK=CHUNK, offset_hz=0)
    sa.plot_frequency_graph(y_mean, x_mean, beans=beans, offset_hz=0)

