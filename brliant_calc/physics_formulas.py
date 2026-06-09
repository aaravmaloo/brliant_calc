import math

def force(m, a):
    return m * a

def kinetic_energy(m, v):
    return 0.5 * m * (v ** 2)

def potential_energy(m, h, g=9.8):
    return m * g * h

def ohms_law(i, r):
    return i * r

def work(f, d):
    return f * d

def speed(d, t):
    if t == 0:
        return "Error: Time cannot be zero."
    return d / t

def acceleration(dv, t):
    if t == 0:
        return "Error: Time cannot be zero."
    return dv / t

def gravitational_force(m1, m2, r):
    G = 6.67430e-11
    return G * m1 * m2 / (r ** 2)

def electric_force(q1, q2, r):
    k = 8.98755e9
    return k * q1 * q2 / (r ** 2)

def momentum(m, v):
    return m * v

def pressure(f, a):
    if a == 0:
        return "Error: Area cannot be zero."
    return f / a

def time_dilation(t, v):
    c = 299792458
    if v >= c:
        return "Error: Velocity must be less than c."
    return t / math.sqrt(1 - (v**2 / c**2))

def energy_mass_equivalence(m):
    c = 299792458
    return m * (c ** 2)

def orbital_velocity(m_central, r):
    G = 6.67430e-11
    return math.sqrt(G * m_central / r)

def escape_velocity(m_planet, r):
    G = 6.67430e-11
    return math.sqrt(2 * G * m_planet / r)
