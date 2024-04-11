import math
import os.path
import numpy as np
import scipy as sp
import soundfile
from matplotlib import pyplot as plt
from sklearn import preprocessing


def plot_magnitude_spectrum(signal, title, sample_rate, frequency_ratio=1):
    ft = sp.fft.rfft(signal)

    magnitude_spectrum = np.abs(ft)
    title = os.path.split(title)[-1]

    # plot magnitude spectrum
    fig = plt.figure(figsize=(18, 5))

    frequency = np.linspace(20, sample_rate, len(magnitude_spectrum)-20)#len(magnitude_spectrum))
    num_frequency_beans = int(len(frequency) * frequency_ratio)

    fig.canvas.manager.set_window_title(title)

    # normalise magnitude
    normalised_magnitude = preprocessing.normalize([magnitude_spectrum])[0]

    # plt.plot(frequency[:num_frequency_beans], magnitude_spectrum[:num_frequency_beans] * (2 / num_frequency_beans))
    plt.plot(frequency[:num_frequency_beans], normalised_magnitude[:num_frequency_beans])
    plt.xlabel("Frequency (Hz)")
    plt.title(title)
    plt.show()
    return fig



def readData(filePath):
    audio_samples, sample_rate = soundfile.read(filePath, dtype='float64')
    return audio_samples, sample_rate


def analyzeSample(filePath):
    audio_samples, sample_rate = readData(filePath)
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





