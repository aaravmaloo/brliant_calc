def force(*args):
    if len(args) != 2:
        return "Error: Force requires mass and acceleration (m, a)."
    m, a = args
    return m * a

def kinetic_energy(*args):
    if len(args) != 2:
        return "Error: Kinetic energy requires mass and velocity (m, v)."
    m, v = args
    return 0.5 * m * (v ** 2)

def potential_energy(*args):
    if len(args) == 2:
        m, h = args
        g = 9.8
    elif len(args) == 3:
        m, g, h = args
    else:
        return "Error: Potential energy requires mass and height (m, h) or (m, g, h)."
    return m * g * h

def ohms_law(*args):
    if len(args) != 2:
        return "Error: Ohm's law requires current and resistance (I, R) to calculate Voltage."
    i, r = args
    return i * r

def work(*args):
    if len(args) != 2:
        return "Error: Work requires force and distance (F, d)."
    f, d = args
    return f * d

def speed(*args):
    if len(args) != 2:
        return "Error: Speed requires distance and time (d, t)."
    d, t = args
    if t == 0:
        return "Error: Time cannot be zero."
    return d / t

def acceleration(*args):
    if len(args) != 2:
        return "Error: Acceleration requires change in velocity and time (dv, t)."
    dv, t = args
    if t == 0:
        return "Error: Time cannot be zero."
    return dv / t
