import math


def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

def sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3

def sphere_surface_area(radius):
    return 4 * math.pi * radius ** 2

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def triangle_area(base, height):
    return 0.5 * base * height

def triangle_area_sss(a, b, c):
    s = (a + b + c) / 2
    area = s * (s - a) * (s - b) * (s - c)
    if area < 0:
        return "Error: Invalid triangle sides."
    return math.sqrt(area)

def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def cone_volume(radius, height):
    return (1 / 3) * math.pi * radius ** 2 * height

def cone_surface_area(radius, height):
    slant = math.sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * (radius + slant)

def pyramid_volume(base_area, height):
    return (1 / 3) * base_area * height

def torus_volume(major_radius, minor_radius):
    return 2 * math.pi ** 2 * major_radius * minor_radius ** 2

def torus_surface_area(major_radius, minor_radius):
    return 4 * math.pi ** 2 * major_radius * minor_radius

def ellipse_area(semi_major, semi_minor):
    return math.pi * semi_major * semi_minor

def ellipse_perimeter(semi_major, semi_minor):
    a, b = semi_major, semi_minor
    return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))

def distance_2d(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def distance_3d(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def midpoint_2d(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def arc_length(radius, angle_degrees):
    return radius * math.radians(angle_degrees)

def sector_area(radius, angle_degrees):
    return 0.5 * radius ** 2 * math.radians(angle_degrees)
