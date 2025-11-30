import matplotlib.pyplot as plt
import numpy as np
import sympy

def plot(func_str, x_range="0,10"):
    try:
        start, end = map(float, x_range.split(","))
        x = np.linspace(start, end, 1000)
        
        # Safe evaluation using numpy
        # We need to make sure numpy functions are available in eval context
        context = {
            "sin": np.sin, "cos": np.cos, "tan": np.tan,
            "exp": np.exp, "log": np.log, "sqrt": np.sqrt,
            "pi": np.pi, "x": x
        }
        
        # Also try to use sympy to convert expression to numpy-compatible lambda if needed
        # But simple eval might be faster for basic strings
        
        y = eval(func_str, {"__builtins__": None}, context)
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y)
        plt.title(f"Plot of {func_str}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()
        return "Plot displayed."
    except Exception as e:
        return f"Error plotting function: {e}"
