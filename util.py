import csv

import numpy as np
from matplotlib import pyplot as plt

def read_signal_from_csv(input_file):
    samples = []

    with open(input_file, mode='r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            for sample in line:
                samples.append(float(sample))

    return samples


def plot_spectogram(fr, ti, sp, file, interval, overlap, hamming):
    plt.pcolormesh(ti, fr, sp , shading='auto')
    plt.title(f'Spektrogram[{file}] - Interval:{interval}, Overlap: {overlap}, Hamming: {hamming}')
    plt.xlabel('Čas [s]')
    plt.ylabel('Frekvenca [Hz]')
    plt.colorbar(label='Amplituda')
    plt.show()


def calculate_rpm(sp, fr):
    # np.max(sp, axis=1) -> max frequency per time bin
    # np.argmax -> max frequenca from all rows
    peak_idx = np.argmax(np.max(sp, axis=1))
    dominant_frequency = fr[peak_idx]
    rpm = (dominant_frequency * 60)
    print(f"Dominant Frequency: {dominant_frequency} Hz")
    print(f"Rpm: {rpm}")
    return rpm