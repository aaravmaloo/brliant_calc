import math
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
    if h_concentration <= 0:
        return "Error: Concentration must be positive."
    return -math.log10(h_concentration)

def h_from_ph(ph):
    return 10 ** (-ph)


def _num(value, name="value"):
    """Convert a numeric input (string or number) to float, raising on failure."""
    try:
        return float(value)
    except (TypeError, ValueError):
        raise ValueError(f"'{value}' is not a valid number for {name}.")


def dilution(c1, v1, c2):
    """M1V1 = M2V2 -> solve for V2 given c1, v1, c2."""
    c1, v1, c2 = _num(c1, "c1"), _num(v1, "v1"), _num(c2, "c2")
    if c2 == 0:
        return "Error: Final concentration (c2) cannot be zero."
    return (c1 * v1) / c2


def molality(moles, solvent_kg):
    """Moles of solute per kilogram of solvent."""
    moles = _num(moles, "moles")
    solvent_kg = _num(solvent_kg, "solvent_kg")
    if solvent_kg == 0:
        return "Error: Solvent mass cannot be zero."
    return moles / solvent_kg


def mole_fraction(moles_a, moles_b):
    """Mole fraction of component A: n_a / (n_a + n_b)."""
    moles_a = _num(moles_a, "moles_a")
    moles_b = _num(moles_b, "moles_b")
    total = moles_a + moles_b
    if total == 0:
        return "Error: Total moles cannot be zero."
    return moles_a / total


def limiting_reagent(*args):
    """Find the limiting reagent from alternating (amount, coefficient) pairs.

    Each reagent contributes two values: the amount available (mol) and its
    stoichiometric coefficient. The reagent with the smallest amount/coefficient
    ratio is limiting. Example: limiting_reagent(10, 2, 6, 1) means reagent 1
    has 10 mol with coefficient 2 and reagent 2 has 6 mol with coefficient 1.
    """
    if len(args) < 4 or len(args) % 2 != 0:
        return "Error: Provide amount/coefficient pairs for at least two reagents."
    reagents = []
    for i in range(0, len(args), 2):
        amount = _num(args[i], f"amount {i // 2 + 1}")
        coeff = _num(args[i + 1], f"coefficient {i // 2 + 1}")
        if coeff <= 0:
            return f"Error: Coefficient {i // 2 + 1} must be positive."
        reagents.append((amount, coeff, amount / coeff))

    limiting = min(reagents, key=lambda r: r[2])
    idx = reagents.index(limiting) + 1
    lines = [
        f"Limiting reagent: Reagent {idx} "
        f"(amount {limiting[0]:g}, coefficient {limiting[1]:g})"
    ]
    for i, (amount, coeff, _ratio) in enumerate(reagents, start=1):
        if i != idx:
            needed = limiting[2] * coeff
            lines.append(
                f"Reagent {i}: {amount:g} available, {needed:g} needed, "
                f"{amount - needed:g} in excess"
            )
    return "\n".join(lines)


def percent_yield(actual, theoretical):
    """Percent yield = (actual / theoretical) * 100."""
    actual = _num(actual, "actual")
    theoretical = _num(theoretical, "theoretical")
    if theoretical == 0:
        return "Error: Theoretical yield cannot be zero."
    return (actual / theoretical) * 100


def boiling_point_elevation(molality, k_b, van_t_hoff=1):
    """dTb = i * Kb * m (van't Hoff factor defaults to 1)."""
    m = _num(molality, "molality")
    kb = _num(k_b, "k_b")
    i = _num(van_t_hoff, "van't Hoff factor")
    return i * kb * m


def freezing_point_depression(molality, k_f, van_t_hoff=1):
    """dTf = i * Kf * m (van't Hoff factor defaults to 1)."""
    m = _num(molality, "molality")
    kf = _num(k_f, "k_f")
    i = _num(van_t_hoff, "van't Hoff factor")
    return i * kf * m


def osmotic_pressure(molarity, temp_kelvin, r=0.0821):
    """Pi = MRT. Temperature must be in Kelvin; R in L*atm/(mol*K)."""
    m = _num(molarity, "molarity")
    t = _num(temp_kelvin, "temperature (K)")
    return m * r * t


def henderson_hasselbalch(pka, ratio):
    """pH = pKa + log10([A-]/[HA])."""
    pka = _num(pka, "pKa")
    ratio = _num(ratio, "ratio")
    if ratio <= 0:
        return "Error: Ratio must be positive."
    return pka + math.log10(ratio)


def half_life(decay_constant):
    """Half-life from decay constant: t1/2 = ln(2) / k."""
    k = _num(decay_constant, "decay constant")
    if k <= 0:
        return "Error: Decay constant must be positive."
    return math.log(2) / k


def radioactive_decay(amount, decay_constant, time):
    """Remaining amount after time t: N = N0 * exp(-k * t)."""
    n0 = _num(amount, "amount")
    k = _num(decay_constant, "decay constant")
    t = _num(time, "time")
    return n0 * math.exp(-k * t)


def density(mass, volume):
    """Density = mass / volume."""
    mass = _num(mass, "mass")
    volume = _num(volume, "volume")
    if volume == 0:
        return "Error: Volume cannot be zero."
    return mass / volume


def ppm_to_concentration(ppm, molar_mass):
    """Convert ppm (mg/L) to molarity (mol/L): M = ppm / (molar_mass * 1000)."""
    ppm = _num(ppm, "ppm")
    mm = _num(molar_mass, "molar mass")
    if mm == 0:
        return "Error: Molar mass cannot be zero."
    return ppm / (mm * 1000)


def molarity_to_ppm(molarity, molar_mass):
    """Convert molarity (mol/L) to ppm (mg/L): ppm = M * molar_mass * 1000."""
    m = _num(molarity, "molarity")
    mm = _num(molar_mass, "molar mass")
    return m * mm * 1000
