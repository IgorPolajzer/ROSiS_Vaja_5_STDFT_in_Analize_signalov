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


def calculate_rpm(fr, sp, t, min_rpm=500, max_rpm=2500):
    spectrum = np.abs(sp[:, t])

    # Hz search limits
    min_hz = min_rpm // 60
    max_hz = max_rpm // 60

    # Find indices in fr array that match the freq bounds.
    valid_indices = np.where((fr >= min_hz) & (fr <= max_hz))[0]

    # Find the freq peak within valid indices
    peak_idx_within_window = np.argmax(spectrum[valid_indices])
    actual_peak_idx = valid_indices[peak_idx_within_window]

    rotational_freq = fr[actual_peak_idx]
    rpm = rotational_freq * 60

    print(f"Motor Rotation Freq (at {t} s): {rotational_freq:.2f} Hz")
    print(f"RPM: {rpm:.1f}")

    return rpm