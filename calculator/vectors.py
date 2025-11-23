import numpy as np
import math

def dot_product(*args):
    n = len(args)
    if n % 2 != 0:
        return "Error: Vectors must have the same number of dimensions."
    mid = n // 2
    v1 = np.array(args[:mid])
    v2 = np.array(args[mid:])
    return np.dot(v1, v2)

def cross_product(*args):
    n = len(args)
    if n != 6:
        return "Error: Cross product requires exactly two 3D vectors (6 components total)."
    v1 = np.array(args[:3])
    v2 = np.array(args[3:])
    return np.cross(v1, v2).tolist()

def magnitude(*args):
    v = np.array(args)
    return np.linalg.norm(v)

def normalize(*args):
    v = np.array(args)
    norm = np.linalg.norm(v)
    if norm == 0:
        return "Error: Cannot normalize zero vector."
    return (v / norm).tolist()

def angle_between(*args):
    n = len(args)
    if n % 2 != 0:
        return "Error: Vectors must have the same number of dimensions."
    mid = n // 2
    v1 = np.array(args[:mid])
    v2 = np.array(args[mid:])
    
    dot = np.dot(v1, v2)
    m1 = np.linalg.norm(v1)
    m2 = np.linalg.norm(v2)
    
    if m1 == 0 or m2 == 0:
        return "Error: Cannot calculate angle with zero vector."
        
    cos_theta = dot / (m1 * m2)

    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    angle_rad = np.arccos(cos_theta)
    return np.degrees(angle_rad)
