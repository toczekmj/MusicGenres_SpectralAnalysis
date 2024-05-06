from itertools import batched
import numpy as np
from Libraries import SoundAnalyzer as sa


def array_splitter(arr: list, chunk_size: int):
    b = batched(arr, chunk_size)
    for chunk in b:
        yield chunk


def matrixize(arr: list):
    if len(arr) > 1:
        first = arr[0]
        last = arr[len(arr)-1]
        if len(first) != len(last):
            arr.remove(last)
    return arr


def calculate_matrix(signal: list, sample_rate: int, CHUNK: int = 100, offset_hz: int = 20):
    if offset_hz >= CHUNK/4:
        raise Exception("You can't offset the plot by more beans, than there are beans in total")

    # Signal is split into chunks of size CHUNK ,
    # and therefore we have to check whether we have some odd last row.
    # If so, we delete that odd part of out matrix, because with large amount of data
    # it won't make any difference
    arr = list(array_splitter(signal, CHUNK))
    arr = matrixize(arr)

    x = []
    y = []

    # Calculate spectrum for every chunk
    for sg in arr:
        magnitude, frequency = sa.calculate_magnitude_spectrum(sg, sample_rate)
        x.append(frequency)
        y.append(magnitude)

    # Convert arrays to matrices, and get mean of every column
    x_matrix = np.matrix(x)
    y_matrix = np.matrix(y)

    # beans = len(x_matrix)
    # return np.squeeze(x_matrix), np.squeeze(y_matrix), beans

    return x, y, len(x)


def matrix_average(signal: list, sample_rate: int, CHUNK: int = 100, offset_hz: int = 20):

    if offset_hz >= CHUNK/4:
        raise Exception("You can't offset the plot by more beans, than there are beans in total")

    # Signal is split into chunks of size CHUNK ,
    # and therefore we have to check whether we have some odd last row.
    # If so, we delete that odd part of out matrix, because with large amount of data
    # it won't make any difference
    arr = list(array_splitter(signal, CHUNK))
    arr = matrixize(arr)

    x = []
    y = []

    # Calculate spectrum for every chunk
    for sg in arr:
        magnitude, frequency = sa.calculate_magnitude_spectrum(sg, sample_rate)
        x.append(frequency)
        y.append(magnitude)

    # Convert arrays to matrices, and get mean of every column
    x_matrix = np.matrix(x)
    y_matrix = np.matrix(y)

    x_mean = np.squeeze(np.asarray(x_matrix.mean(0)))
    y_mean = np.squeeze(np.asarray(y_matrix.mean(0)))
    beans = len(x_mean)
    return x_mean, y_mean, beans
