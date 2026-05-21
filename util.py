import csv

from matplotlib import pyplot as plt
import numpy as np

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

