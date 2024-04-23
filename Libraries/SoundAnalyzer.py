import librosa
import numpy as np
import scipy as sp
from sklearn import preprocessing


def calculate_magnitude_spectrum(signal: list, sample_rate: int = 22050):
    # perform transformation using Fast Fourier Transform
    # for purely real input DFT output is 'mirrored'
    # therefore we can use rfft instead of fft to cut out
    # the mirrored part we are not interested of
    fourier_transform = sp.fft.rfft(signal)

    # get only the real parts of above solution
    magnitude_spectrum = np.abs(fourier_transform)

    # normalise magnitude
    normalised_magnitude_spectrum = preprocessing.normalize([magnitude_spectrum], norm='max')[0]

    # create frequency linspace ( offset_hz < frequency < len(mag_spec)-offset_hz
    # to prevent artifacts
    frequency = np.linspace(
        0,
        sample_rate,
        len(magnitude_spectrum)
    )

    return normalised_magnitude_spectrum, frequency


def load_song(path: str, sample_rate: int = 22050):
    # librosa uses 22050 resampling by default
    # which is good for our further computation steps
    # resulting in lower memory consumption and faster operations
    music, sample_rate = librosa.load(path, sr=sample_rate)
    return music, sample_rate
