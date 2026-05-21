from stdft import stdft
from util import plot_spectogram, calculate_rpm

if __name__ == '__main__':
    file = "naloga_1_rpm/sig3.csv"
    interval = 1
    overlap = 0.0
    hamming = True

    fr, ti, sp = stdft(file, interval, overlap, hamming_window=hamming)
    calculate_rpm(sp, fr)
    plot_spectogram(fr, ti, sp, file, interval, overlap, hamming)