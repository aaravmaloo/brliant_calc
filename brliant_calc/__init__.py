"""
Brliant Calculator - A powerful command-line scientific calculator

A comprehensive calculator for engineers, scientists, and developers with support for:
- Basic and advanced mathematics
- Vector and matrix operations
- Complex numbers and symbolic math
- Physics formulas and unit conversions
- Currency conversion
- Graphing and plotting
- Dimensional analysis
- Arbitrary precision arithmetic
- Number theory (primes, GCD, LCM, Fibonacci, Euler totient)
- Combinatorics (permutations, combinations, Stirling, Bell numbers)
- Extended statistics (mode, correlation, kurtosis, confidence intervals)
- Geometry (circles, spheres, cones, tori, ellipses, distances)
- Financial math (compound interest, EMI, NPV, ROI, annuities)
- Signal processing (FFT, autocorrelation, windowing, spectrograms)
- Calculus (Taylor series, numerical diff/integration, limits, gradients)
- Equation solving (quadratic, cubic, bisection, Newton-Raphson)
- Expression evaluation (safe AST-based math expression parser)
- Calculation history (save, search, export, stats)
- Date & time math (add days/months, date differences, weekdays, Julian days, ages)
"""

__version__ = "4.2.0"
__author__ = "Aarav Maloo"
__email__ = "aaravmaloo06@gmail.com"
__description__ = "A powerful CLI scientific calculator with number theory, combinatorics, geometry, finance, signal processing, calculus, equation solving, and more."

from brliant_calc.__main__ import main

__all__ = ["main", "__version__"]
