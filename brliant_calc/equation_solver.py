import sympy
import numpy as np


def quadratic(a, b, c):
    a, b, c = float(a), float(b), float(c)
    if a == 0:
        if b == 0:
            return "Error: Not a valid equation."
        return -c / b
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return {"roots": [x1, x2], "type": "real and distinct"}
    elif discriminant == 0:
        x = -b / (2 * a)
        return {"roots": [x], "type": "real and equal"}
    else:
        real = -b / (2 * a)
        imag = (abs(discriminant) ** 0.5) / (2 * a)
        return {"roots": [complex(real, imag), complex(real, -imag)], "type": "complex"}

def cubic(a, b, c, d):
    x = sympy.Symbol('x')
    eq = float(a) * x**3 + float(b) * x**2 + float(c) * x + float(d)
    roots = sympy.solve(eq, x)
    return [complex(r) for r in roots]

def polynomial_roots(coeffs):
    coeffs = [float(c) for c in coeffs]
    return np.roots(coeffs).tolist()

def linear_system_2d(a1, b1, c1, a2, b2, c2):
    A = np.array([[float(a1), float(b1)], [float(a2), float(b2)]])
    b = np.array([float(c1), float(c2)])
    det = np.linalg.det(A)
    if abs(det) < 1e-12:
        return "Error: System has no unique solution (determinant is zero)."
    x = np.linalg.solve(A, b)
    return {"x": x[0], "y": x[1]}

def simultaneous_2d(a1, b1, c1, a2, b2, c2):
    return linear_system_2d(a1, b1, c1, a2, b2, c2)

def linear_system_3d(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    A = np.array([
        [float(a1), float(b1), float(c1)],
        [float(a2), float(b2), float(c2)],
        [float(a3), float(b3), float(c3)]
    ])
    b = np.array([float(d1), float(d2), float(d3)])
    det = np.linalg.det(A)
    if abs(det) < 1e-12:
        return "Error: System has no unique solution (determinant is zero)."
    x = np.linalg.solve(A, b)
    return {"x": x[0], "y": x[1], "z": x[2]}

def bisection(func_str, a, b, tol=1e-8, max_iter=100):
    x = sympy.Symbol('x')
    expr = sympy.sympify(func_str)
    f = sympy.lambdify(x, expr, modules=['numpy'])
    a, b = float(a), float(b)
    if f(a) * f(b) >= 0:
        return "Error: f(a) and f(b) must have opposite signs."
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def newton_raphson(func_str, x0, tol=1e-8, max_iter=100):
    x = sympy.Symbol('x')
    expr = sympy.sympify(func_str)
    f = sympy.lambdify(x, expr, modules=['numpy'])
    df_expr = sympy.diff(expr, x)
    df = sympy.lambdify(x, df_expr, modules=['numpy'])
    x_val = float(x0)
    for _ in range(max_iter):
        fx = f(x_val)
        dfx = df(x_val)
        if abs(dfx) < 1e-15:
            return "Error: Derivative is zero."
        x_new = x_val - fx / dfx
        if abs(x_new - x_val) < tol:
            return x_new
        x_val = x_new
    return x_val

def secant_method(func_str, x0, x1, tol=1e-8, max_iter=100):
    x = sympy.Symbol('x')
    expr = sympy.sympify(func_str)
    f = sympy.lambdify(x, expr, modules=['numpy'])
    x0, x1 = float(x0), float(x1)
    for _ in range(max_iter):
        f0, f1 = f(x0), f(x1)
        if abs(f1 - f0) < 1e-15:
            return "Error: Division by zero in secant method."
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    return x1
