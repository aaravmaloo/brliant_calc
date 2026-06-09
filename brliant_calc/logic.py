import sympy
from sympy.logic import simplify_logic
from sympy.logic.boolalg import truth_table as sympy_truth_table
from sympy.abc import A, B, C, D, E, F

def base_convert(number_str, from_base, to_base):
    try:
        decimal_val = int(str(number_str), int(from_base))
    except ValueError:
        return f"Error: '{number_str}' is not a valid number in base {from_base}"
    
    if int(to_base) == 10:
        return str(decimal_val)
    
    def _from_decimal(n, base):
        if n == 0:
            return "0"
        digits = "0123456789ABCDEF"
        res = ""
        while n:
            res = digits[n % base] + res
            n //= base
        return res
    
    return _from_decimal(decimal_val, int(to_base))

def truth_table(expr_str):
    try:
        expr = sympy.sympify(expr_str)
        vars = sorted(expr.free_symbols, key=lambda s: s.name)
        table = list(sympy_truth_table(expr, vars))
        
        header = [v.name for v in vars] + ["Result"]
        rows = []
        for inputs, result in table:
            rows.append([int(i) for i in inputs] + [int(result)])
            
        return {"header": header, "rows": rows}
    except Exception as e:
        return f"Error: {e}"

def simplify_boolean(expr_str):
    try:
        expr = sympy.sympify(expr_str)
        simplified = simplify_logic(expr)
        return str(simplified)
    except Exception as e:
        return f"Error: {e}"

def bitwise_and(a, b):
    return int(a) & int(b)

def bitwise_or(a, b):
    return int(a) | int(b)

def bitwise_xor(a, b):
    return int(a) ^ int(b)

def bitwise_not(a):
    return ~int(a)
