from math import ceil

import numpy as np

from util import *


def stdft(file_name, interval_length, overlap_percentage, nfft=1024, hamming_window=False, Fs=256):
    samples = read_signal_from_csv(file_name)

    # 1. Split signal into parts.
    windows = []
    t = []
    sp = []
    number_of_samples = int(interval_length * Fs)

    idx = 0
    while idx < len(samples) - 1:
        if idx + number_of_samples <= len(samples):
            second_idx = idx + number_of_samples
        else:
            second_idx = len(samples)

        window = samples[idx:second_idx]

        # 1.2 Apply hamming window.
        if hamming_window:
            window = window * np.hamming(len(window))

        # 1.3 Pad the samples.
        if len(window) < nfft:
            window = np.pad(window, (0, nfft - len(window)))

        # Caluculate end of window in seconds.
        t.append((idx + number_of_samples) / Fs)

        # Calculate FFT.
        window = np.fft.fft(window)

        # Calculate the power spectral density (|X(tao, window)|²).
        sp.append(np.abs(window[:nfft // 2 + 1]) ** 2)

        windows.append(window)
        idx += ceil(number_of_samples - overlap_percentage * number_of_samples)

    # Get all frequency bin centers based on the sample rate and window length.
    f = np.fft.rfftfreq(nfft, d=1 / Fs)

    return f, np.array(t), np.array(sp).T
