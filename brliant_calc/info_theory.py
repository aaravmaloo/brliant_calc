import numpy as np
from scipy.stats import entropy as scipy_entropy

def shannon_entropy(probabilities):
    probabilities = np.array(probabilities, dtype=float)
    if not np.isclose(np.sum(probabilities), 1.0):
        probabilities = probabilities / np.sum(probabilities)
    return scipy_entropy(probabilities, base=2)

def kl_divergence(p, q):
    p = np.array(p, dtype=float)
    q = np.array(q, dtype=float)
    return scipy_entropy(p, q, base=2)

def hamming_distance(s1, s2):
    s1, s2 = str(s1), str(s2)
    if len(s1) != len(s2):
        return "Error: Strings must be of equal length"
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def levenshtein_distance(s1, s2):
    s1, s2 = str(s1), str(s2)
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

def cross_entropy(p, q):
    p = np.array(p, dtype=float)
    q = np.array(q, dtype=float)
    return -np.sum(p * np.log2(q))

def mutual_information(p_xy):
    """
    Compute mutual information from a joint probability distribution matrix.
    """
    p_xy = np.array(p_xy, dtype=float)
    p_x = np.sum(p_xy, axis=1)
    p_y = np.sum(p_xy, axis=0)
    
    mi = 0
    for i in range(len(p_x)):
        for j in range(len(p_y)):
            if p_xy[i, j] > 0:
                mi += p_xy[i, j] * np.log2(p_xy[i, j] / (p_x[i] * p_y[j]))
    return mi
