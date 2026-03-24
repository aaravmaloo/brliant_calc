import numpy as np
import math
from functools import lru_cache

def dot_product(v1, v2):
    return np.dot(v1, v2)

def cross_product(v1, v2):
    return np.cross(v1, v2).tolist()

def magnitude(v):
    return np.linalg.norm(v)

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return "Error: Cannot normalize zero vector."
    return (v / norm).tolist()

def angle_between(v1, v2):
    v1_u = normalize(v1)
    v2_u = normalize(v2)

    if isinstance(v1_u, str) or isinstance(v2_u, str):
        return "Error: Cannot calculate angle with zero vector."

    return np.degrees(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)))

def vector_projection(u, v):
    """Project vector v onto vector u"""
    if magnitude(u) == 0:
        return "Error: Cannot project onto zero vector."
    projection_coeff = np.dot(v, u) / np.dot(u, u)
    return projection_coeff * u

def vector_rejection(u, v):
    """Get component of v orthogonal to u (rejection)"""
    proj = vector_projection(u, v)
    return v - proj

def vector_sum(vectors):
    """Sum multiple vectors"""
    return np.sum(vectors, axis=0)

def vector_subtract(v1, v2):
    """Subtract v2 from v1"""
    return v1 - v2

def scalar_multiply(scalar, v):
    """Multiply vector by scalar"""
    return scalar * v

def vector_distance(v1, v2):
    """Euclidean distance between two vectors"""
    return magnitude(v1 - v2)

def vector_angle_3d(v1, v2):
    """Calculate angle between two 3D vectors"""
    dot = np.dot(v1, v2)
    mag1 = magnitude(v1)
    mag2 = magnitude(v2)

    if mag1 == 0 or mag2 == 0:
        return "Error: Cannot calculate angle with zero vector."

    cos_angle = dot / (mag1 * mag2)
    return np.degrees(np.arccos(np.clip(cos_angle, -1.0, 1.0)))

def vector_cross_matrix(v):
    """Create skew-symmetric matrix for cross product multiplication"""
    if len(v) != 3:
        return "Error: Cross product matrix only defined for 3D vectors"
    return np.array([
        [0, -v[2], v[1]],
        [v[2], 0, -v[0]],
        [-v[1], v[0], 0]
    ])

def vector_is_parallel(v1, v2, tol=1e-10):
    """Check if two vectors are parallel"""
    if magnitude(v1) == 0 or magnitude(v2) == 0:
        return "Error: Cannot check parallelism with zero vectors"

    cross = np.cross(v1, v2)
    return np.linalg.norm(cross) < tol

def vector_is_orthogonal(v1, v2, tol=1e-10):
    """Check if two vectors are orthogonal"""
    return abs(np.dot(v1, v2)) < tol

def vector_area_triangle(v1, v2):
    """Calculate area of parallelogram spanned by two vectors"""
    return magnitude(np.cross(v1, v2))

def vector_volume_parallelepiped(v1, v2, v3):
    """Calculate volume of parallelepiped spanned by three vectors"""
    return abs(np.dot(v1, np.cross(v2, v3)))

def vector_normalize_2d(v):
    """Normalize 2D vector and return angle"""
    if len(v) != 2:
        return "Error: normalize_2d requires 2D vector"
    norm = magnitude(v)
    if norm == 0:
        return "Error: Cannot normalize zero vector"
    angle = np.arctan2(v[1], v[0])
    return (v / norm).tolist(), np.degrees(angle)

@lru_cache(maxsize=128)
def vector_max_component(v):
    """Find index of maximum component in vector"""
    return np.argmax(v)

def vector_min_component(v):
    """Find index of minimum component in vector"""
    return np.argmin(v)

def vector_range(v):
    """Calculate range (max - min) of vector components"""
    return np.max(v) - np.min(v)
