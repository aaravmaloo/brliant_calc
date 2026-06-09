import re

ELEMENTS = {
    'H': 1.008, 'He': 4.0026, 'Li': 6.94, 'Be': 9.0122, 'B': 10.81, 'C': 12.011,
    'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.180, 'Na': 22.990, 'Mg': 24.305,
    'Al': 26.982, 'Si': 28.085, 'P': 30.974, 'S': 32.06, 'Cl': 35.45, 'Ar': 39.948,
    'K': 39.098, 'Ca': 40.078, 'Fe': 55.845, 'Cu': 63.546, 'Zn': 65.38, 'Ag': 107.87,
    'Au': 196.97, 'Hg': 200.59, 'Pb': 207.2, 'U': 238.03
}

def molar_mass(formula):
    def parse_formula(f):
        res = {}
        for el, count in re.findall(r'([A-Z][a-z]?)(\d*)', f):
            count = int(count) if count else 1
            res[el] = res.get(el, 0) + count
        return res

    parts = parse_formula(formula)
    total = 0.0
    for el, count in parts.items():
        if el in ELEMENTS:
            total += ELEMENTS[el] * count
        else:
            return f"Error: Element '{el}' not found in database."
    return total

def ideal_gas_law(p=None, v=None, n=None, t=None):
    """PV = nRT. R = 0.0821 L*atm/(mol*K)"""
    R = 0.0821
    if sum(x is None for x in (p, v, n, t)) != 1:
        return "Error: Provide exactly three of P, V, n, T."
    
    if p is None: return (n * R * t) / v
    if v is None: return (n * R * t) / p
    if n is None: return (p * v) / (R * t)
    if t is None: return (p * v) / (n * R)

def molarity(moles, volume):
    if volume == 0:
        return "Error: Volume cannot be zero."
    return moles / volume

def ph_from_h(h_concentration):
    import math
    if h_concentration <= 0:
        return "Error: Concentration must be positive."
    return -math.log10(h_concentration)

def h_from_ph(ph):
    return 10 ** (-ph)
