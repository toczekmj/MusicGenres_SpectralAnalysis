import librosa
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from sklearn import preprocessing


def calculate_magnitude_spectrum(signal, sample_rate=22050, offset_hz=20):
    # perform transformation using Fast Fourier Transform
    # for purely real input DFT output is 'mirrored'
    # therefore we can use rfft instead of fft to cut out
    # the mirrored part we are not interested of
    fourier_transform = sp.fft.rfft(signal)

    # get only the real parts of above solution
    magnitude_spectrum = np.abs(fourier_transform)

    # normalise magnitude
    normalised_magnitude_spectrum = preprocessing.normalize([magnitude_spectrum])[0]

    # create frequency linspace ( offset_hz < frequency < len(mag_spec)-offset_hz
    # to prevent artifacts
    frequency = np.linspace(
        offset_hz,
        # 16000,
        sample_rate,
        len(magnitude_spectrum)
    )

    # calculate amount of beans
    beans_amount = len(frequency) - offset_hz

    return normalised_magnitude_spectrum, frequency, beans_amount


def plot_frequency_graph(magnitude_spectrum, frequency, beans_amount, offset_hz=20, size_x=18, size_y=5):
    plt.figure(
        figsize=(size_x, size_y)
    )

    plt.plot(
        frequency[offset_hz:beans_amount],
        magnitude_spectrum[offset_hz:beans_amount]
    )

    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Normalised average value of ĝ(x)")
    plt.title("Average frequency of music")
    plt.show()


def load_song(path, sample_rate=22050):
    # librosa uses 22050 resampling by default
    # which is good for our further computation steps
    # resulting in lower memory consumption and faster operations
    music, sample_rate = librosa.load(path, sr=sample_rate)
    return music, sample_rate


def print_analyze_sample(filePath):
    audio_samples, sample_rate = load_song(filePath)
    print("sample rate", sample_rate)
    number_samples = len(audio_samples)

    # audio samples matrix
    print(f'Audio samples {audio_samples}')

    # number of samples
    print(f'Number of samples {number_samples}')

    # sample rate
    print(f'Sample rate {sample_rate}')

    # duration
    duration = round(number_samples / sample_rate, 2)
    print(f'Audio duration: {duration}')





