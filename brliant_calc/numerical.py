import numpy as np
from scipy.interpolate import lagrange, CubicSpline
import sympy

def polynomial_fit(x, y, degree):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    coeffs = np.polyfit(x, y, int(degree))
    return coeffs.tolist()

def lagrange_interpolation(x, y, x_val):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    poly = lagrange(x, y)
    return float(poly(float(x_val)))

def cubic_spline_interpolation(x, y, x_val):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    cs = CubicSpline(x, y)
    return float(cs(float(x_val)))

def rk4_solve(func_str, y0, t_start, t_end, steps, var_y="y", var_t="t"):
    """
    Solves dy/dt = f(t, y) using RK4 method.
    """
    y = sympy.Symbol(var_y)
    t = sympy.Symbol(var_t)
    expr = sympy.sympify(func_str)
    f = sympy.lambdify((t, y), expr, modules=['numpy'])
    
    t_val = float(t_start)
    y_val = float(y0)
    h = (float(t_end) - t_val) / int(steps)
    
    results = [(t_val, y_val)]
    for _ in range(int(steps)):
        k1 = h * f(t_val, y_val)
        k2 = h * f(t_val + 0.5 * h, y_val + 0.5 * k1)
        k3 = h * f(t_val + 0.5 * h, y_val + 0.5 * k2)
        k4 = h * f(t_val + h, y_val + k3)
        
        y_val += (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        t_val += h
        results.append((t_val, y_val))
    
    return results

def newton_interpolation(x, y, x_val):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])
            
    # Evaluate at x_val
    p = coef[0, n - 1]
    for i in range(n - 2, -1, -1):
        p = coef[0, i] + (float(x_val) - x[i]) * p
    return p
