import numpy as np
from scipy import stats

def normal_pdf(x, mu=0, sigma=1):
    return stats.norm.pdf(float(x), loc=float(mu), scale=float(sigma))

def normal_cdf(x, mu=0, sigma=1):
    return stats.norm.cdf(float(x), loc=float(mu), scale=float(sigma))

def normal_ppf(p, mu=0, sigma=1):
    return stats.norm.ppf(float(p), loc=float(mu), scale=float(sigma))

def binomial_pmf(k, n, p):
    return stats.binom.pmf(int(k), int(n), float(p))

def binomial_cdf(k, n, p):
    return stats.binom.cdf(int(k), int(n), float(p))

def poisson_pmf(k, lam):
    return stats.poisson.pmf(int(k), float(lam))

def poisson_cdf(k, lam):
    return stats.poisson.cdf(int(k), float(lam))

def exponential_pdf(x, lam):
    return stats.expon.pdf(float(x), scale=1.0/float(lam))

def t_test_1samp(data, popmean):
    data = np.array(data, dtype=float)
    t_stat, p_val = stats.ttest_1samp(data, float(popmean))
    return {"t_statistic": t_stat, "p_value": p_val}

def t_test_ind(data1, data2):
    data1 = np.array(data1, dtype=float)
    data2 = np.array(data2, dtype=float)
    t_stat, p_val = stats.ttest_ind(data1, data2)
    return {"t_statistic": t_stat, "p_value": p_val}

def sample_normal(n, mu=0, sigma=1):
    return np.random.normal(float(mu), float(sigma), int(n)).tolist()

def sample_binomial(n, trials, p):
    return np.random.binomial(int(trials), float(p), int(n)).tolist()
