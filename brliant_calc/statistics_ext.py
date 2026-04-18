import numpy as np
from collections import Counter


def mode(*args):
    if not args:
        return "Error: No data provided."
    counts = Counter(args)
    max_count = max(counts.values())
    modes = [val for val, count in counts.items() if count == max_count]
    if len(modes) == 1:
        return modes[0]
    return modes

def percentile(data, p):
    return np.percentile(data, p)

def correlation(x, y):
    if len(x) != len(y):
        return "Error: Arrays must have the same length."
    return np.corrcoef(x, y)[0, 1]

def covariance(x, y):
    if len(x) != len(y):
        return "Error: Arrays must have the same length."
    return np.cov(x, y, ddof=1)[0, 1]

def skewness(*args):
    if len(args) < 3:
        return "Error: Skewness requires at least 3 data points."
    n = len(args)
    mean = np.mean(args)
    std = np.std(args, ddof=1)
    if std == 0:
        return "Error: Standard deviation is zero."
    return np.sum(((args - mean) / std) ** 3) * n / ((n - 1) * (n - 2))

def kurtosis(*args):
    if len(args) < 4:
        return "Error: Kurtosis requires at least 4 data points."
    n = len(args)
    mean = np.mean(args)
    std = np.std(args, ddof=1)
    if std == 0:
        return "Error: Standard deviation is zero."
    m4 = np.mean(((args - mean) / std) ** 4)
    return m4 - 3

def geometric_mean(*args):
    if any(a <= 0 for a in args):
        return "Error: Geometric mean requires positive values."
    return np.exp(np.mean(np.log(args)))

def harmonic_mean(*args):
    if any(a == 0 for a in args):
        return "Error: Harmonic mean requires non-zero values."
    return len(args) / np.sum(1.0 / np.array(args))

def z_score(x, mean, std):
    if std == 0:
        return "Error: Standard deviation cannot be zero."
    return (x - mean) / std

def chi_square(observed, expected):
    observed = np.array(observed, dtype=float)
    expected = np.array(expected, dtype=float)
    if observed.shape != expected.shape:
        return "Error: Observed and expected must have the same shape."
    if np.any(expected == 0):
        return "Error: Expected values must be non-zero."
    return np.sum((observed - expected) ** 2 / expected)

def iqr(*args):
    q1 = np.percentile(args, 25)
    q3 = np.percentile(args, 75)
    return q3 - q1

def range_val(*args):
    return max(args) - min(args)

def coefficient_of_variation(*args):
    mean = np.mean(args)
    if mean == 0:
        return "Error: Mean is zero."
    return (np.std(args, ddof=1) / mean) * 100

def weighted_mean(values, weights):
    values = np.array(values, dtype=float)
    weights = np.array(weights, dtype=float)
    if len(values) != len(weights):
        return "Error: Values and weights must have the same length."
    return np.average(values, weights=weights)

def moving_average(data, window):
    data = np.array(data, dtype=float)
    if window <= 0 or window > len(data):
        return "Error: Invalid window size."
    return np.convolve(data, np.ones(window) / window, mode='valid')

def confidence_interval(*args, confidence=0.95):
    from scipy import stats
    n = len(args)
    mean = np.mean(args)
    se = np.std(args, ddof=1) / np.sqrt(n)
    h = se * stats.t.ppf((1 + confidence) / 2, n - 1)
    return (mean - h, mean + h)
