import sympy
import numpy as np
from math import factorial


def taylor_series(expr_str, var="x", point=0, order=6):
    x = sympy.Symbol(var)
    expr = sympy.sympify(expr_str)
    return sympy.series(expr, x, point, order)

def numerical_diff(func_str, x_val, h=1e-7, var="x"):
    x = sympy.Symbol(var)
    expr = sympy.sympify(func_str)
    f = sympy.lambdify(x, expr, modules=['numpy'])
    return (f(x_val + h) - f(x_val - h)) / (2 * h)

def numerical_integrate(func_str, a, b, var="x"):
    x = sympy.Symbol(var)
    expr = sympy.sympify(func_str)
    f = sympy.lambdify(x, expr, modules=['numpy'])
    n = 10000
    dx = (b - a) / n
    x_vals = np.linspace(a, b, n + 1)
    y_vals = f(x_vals)
    return float(np.trapz(y_vals, x_vals))

def series_sum(expr_str, start, end, var="n"):
    n = sympy.Symbol(var, integer=True)
    expr = sympy.sympify(expr_str)
    total = sympy.summation(expr, (n, int(start), int(end)))
    return total

def limit(expr_str, point, var="x", direction='+'):
    x = sympy.Symbol(var)
    expr = sympy.sympify(expr_str)
    return sympy.limit(expr, x, float(point), dir=direction)

def partial_diff(expr_str, *variables):
    expr = sympy.sympify(expr_str)
    result = expr
    for var in variables:
        result = sympy.diff(result, sympy.Symbol(var))
    return result

def double_integrate(expr_str, var1="x", var2="y", bounds1=None, bounds2=None):
    x, y = sympy.symbols(f'{var1} {var2}')
    expr = sympy.sympify(expr_str)
    if bounds1 and bounds2:
        return sympy.integrate(expr, (x, bounds1[0], bounds1[1]), (y, bounds2[0], bounds2[1]))
    elif bounds1:
        return sympy.integrate(expr, (x, bounds1[0], bounds1[1]))
    return sympy.integrate(expr, x, y)

def maclaurin_series(expr_str, order=6, var="x"):
    return taylor_series(expr_str, var=var, point=0, order=order)

def gradient(expr_str, variables=None):
    if variables is None:
        variables = ['x', 'y', 'z']
    symbols = [sympy.Symbol(v) for v in variables]
    expr = sympy.sympify(expr_str)
    return [sympy.diff(expr, s) for s in symbols]

def jacobian(func_strs, variables=None):
    if variables is None:
        variables = ['x', 'y', 'z']
    symbols = [sympy.Symbol(v) for v in variables]
    exprs = [sympy.sympify(f) for f in func_strs.split(',')]
    j = []
    for expr in exprs:
        row = [sympy.diff(expr, s) for s in symbols]
        j.append(row)
    return sympy.Matrix(j)
