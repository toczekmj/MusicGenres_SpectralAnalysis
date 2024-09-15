from matplotlib import pyplot as plt


def plot_frequency_graph_semilog(frequency: list, magnitude_spectrum: list, beans: int,
                         size_x: int = 18, size_y: int = 5, offset_hz: int = 50):
    plt.figure(
        figsize=(size_x, size_y)
    )

    x_axis = frequency[int(offset_hz/2):int(beans-offset_hz/2)]
    y_axis = magnitude_spectrum[int(offset_hz/2):int(beans-offset_hz/2)]

    plt.semilogy(
        x_axis,
        y_axis
    )

    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude ĝ(x)")
    plt.title("Average frequency of music")
    plt.show()


def plot_frequency_graph(frequency: list, magnitude_spectrum: list, beans: int,
                         size_x: int = 18, size_y: int = 5, offset_hz: int = 50):
    plt.figure(
        figsize=(size_x, size_y)
    )

    x_axis = frequency[int(offset_hz/2):int(beans-offset_hz/2)]
    y_axis = magnitude_spectrum[int(offset_hz/2):int(beans-offset_hz/2)]

    plt.plot(
        x_axis,
        y_axis
    )

    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude ĝ(x)")
    plt.title("Average frequency of music")
    plt.show()
