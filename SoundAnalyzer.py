import numpy, scipy, soundfile, pylab, matplotlib, wave
from numpy import arange
from numpy import fft as numpyfft

# matplotlib.use('tkagg')

# def analyzeSample(filePath):
    # audio_samples, sample_rate = soundfile.read(filePath, dtype='int32')
    # print("sample rate", sample_rate)
    # number_samples = len(audio_samples)

    # audio samples matrux
    # print(f'Audio samples {audio_samples}')

    # number of samples
    # print(f'Number of samples {number_samples}')

    # sample rate
    # print(f'Sample rate {sample_rate}')

    # duration
    # duration = round(number_samples / sample_rate, 2)
    # print(f'Audio duration: {duration}')
    #
    # # list of possible frequencies
    # freq_bins = arange(number_samples//2) * sample_rate / number_samples
    # print(f'Frequency length: {len(freq_bins)}')
    # print(f'Frequency bins: {freq_bins}')

    # fft_data = numpyfft.fft(audio_samples)
    # print(f'FFT Length: {len(fft_data)}')
    # print(f'FFT Data: {fft_data}')
    #
    # x_axis_data = freq_bins
    # y_axis_data = fft_data
    #
    # pylab.plot(x_axis_data, y_axis_data)





