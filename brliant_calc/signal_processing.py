import numpy as np


def fft(signal):
    signal = np.array(signal, dtype=complex)
    return np.fft.fft(signal)

def ifft(spectrum):
    spectrum = np.array(spectrum, dtype=complex)
    return np.fft.ifft(spectrum)

def moving_average(signal, window_size):
    signal = np.array(signal, dtype=float)
    if window_size <= 0 or window_size > len(signal):
        return "Error: Invalid window size."
    return np.convolve(signal, np.ones(window_size) / window_size, mode='valid')

def power_spectrum(signal, sample_rate=1.0):
    signal = np.array(signal, dtype=float)
    n = len(signal)
    fft_vals = np.fft.fft(signal)
    power = np.abs(fft_vals) ** 2 / n
    freqs = np.fft.fftfreq(n, d=1.0 / sample_rate)
    return {"frequencies": freqs[:n//2].tolist(), "power": power[:n//2].tolist()}

def autocorrelation(signal):
    signal = np.array(signal, dtype=float)
    mean = np.mean(signal)
    centered = signal - mean
    result = np.correlate(centered, centered, mode='full')
    result = result[len(result)//2:]
    if result[0] != 0:
        result = result / result[0]
    return result

def cross_correlation(signal1, signal2):
    signal1 = np.array(signal1, dtype=float)
    signal2 = np.array(signal2, dtype=float)
    return np.correlate(signal1, signal2, mode='full')

def hamming_window(n):
    return np.hamming(int(n)).tolist()

def hanning_window(n):
    return np.hanning(int(n)).tolist()

def blackman_window(n):
    return np.blackman(int(n)).tolist()

def spectrogram_data(signal, window_size, hop_size, sample_rate=1.0):
    signal = np.array(signal, dtype=float)
    n = len(signal)
    num_frames = max(1, (n - window_size) // hop_size + 1)
    spec = []
    for i in range(num_frames):
        start = i * hop_size
        end = start + window_size
        if end > n:
            break
        frame = signal[start:end] * np.hanning(window_size)
        fft_vals = np.fft.fft(frame)
        power = np.abs(fft_vals[:window_size//2]) ** 2
        spec.append(power.tolist())
    return spec
