import numpy as np
import ast
import scipy

def parse_matrix(matrix_str):
  
    try:
  
        matrix_list = ast.literal_eval(matrix_str)
        if isinstance(matrix_list, list):
             return np.array(matrix_list)
    
        if isinstance(matrix_list, tuple):
             return np.array(matrix_list)
    except:
        pass
    
   
    try:
        if not matrix_str.strip().startswith("[["):
             matrix_str = f"[{matrix_str}]"
        matrix_list = ast.literal_eval(matrix_str)
        return np.array(matrix_list)
    except Exception as e:
        raise ValueError(f"Invalid matrix format: {e}")

def mul(m1_str, m2_str):
    m1 = parse_matrix(m1_str)
    m2 = parse_matrix(m2_str)
    return np.matmul(m1, m2)

def det(m_str):
    m = parse_matrix(m_str)
    return np.linalg.det(m)

def inv(m_str):
    m = parse_matrix(m_str)
    return np.linalg.inv(m)

def eig(m_str):
    m = parse_matrix(m_str)
    w, v = np.linalg.eig(m)
    return f"Eigenvalues:\n{w}\n\nEigenvectors:\n{v}"

def transpose(m_str):
    m = parse_matrix(m_str)
    return m.T

def rank(m_str):
    m = parse_matrix(m_str)
    return np.linalg.matrix_rank(m)

def lu_decomposition(m_str):
    m = parse_matrix(m_str)
    from scipy.linalg import lu
    P, L, U = lu(m)
    return f"P:\n{P}\n\nL:\n{L}\n\nU:\n{U}"

def qr_decomposition(m_str):
    m = parse_matrix(m_str)
    Q, R = np.linalg.qr(m)
    return f"Q:\n{Q}\n\nR:\n{R}"

def cholesky_decomposition(m_str):
    m = parse_matrix(m_str)
    L = np.linalg.cholesky(m)
    return f"L:\n{L}"

def svd_decomposition(m_str):
    m = parse_matrix(m_str)
    U, S, V = np.linalg.svd(m)
    return f"U:\n{U}\n\nS:\n{S}\n\nV:\n{V}"

def solve_linear_system(A_str, b_str):
    A = parse_matrix(A_str)
    b = parse_matrix(b_str)
    x = np.linalg.solve(A, b)
    return x

def least_squares(A_str, b_str):
    A = parse_matrix(A_str)
    b = parse_matrix(b_str)
    x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
    return f"Solution:\n{x}\n\nResiduals:\n{residuals}\n\nRank:\n{rank}\n\nSingular values:\n{s}"

def null_space(m_str):
    m = parse_matrix(m_str)
    from scipy.linalg import null_space
    ns = null_space(m)
    return ns

def condition_number(m_str):
    m = parse_matrix(m_str)
    return np.linalg.cond(m)

def matrix_exponential(m_str):
    m = parse_matrix(m_str)
    from scipy.linalg import expm
    return expm(m)

def sylvester_equation(A_str, B_str, C_str):
    A = parse_matrix(A_str)
    B = parse_matrix(B_str)
    C = parse_matrix(C_str)
    from scipy.linalg import solve_sylvester
    X = solve_sylvester(A, B, C)
    return X


def matrix_power(m_str, n):
    m = parse_matrix(m_str)
    return np.linalg.matrix_power(m, n)

def determinant_via_lu(m_str):
    m = parse_matrix(m_str)
    from scipy.linalg import lu
    _, L, U = lu(m)
    det = np.prod(np.diag(L)) * np.prod(np.diag(U))
    return det

def inverse_via_lu(m_str):
    m = parse_matrix(m_str)
    from scipy.linalg import lu_factor, lu_solve
    lu, piv = lu_factor(m)
    identity = np.eye(m.shape[0])
    inv = lu_solve((lu, piv), identity)
    return inv

def matrix_logarithm(m_str):
    m = parse_matrix(m_str)
    from scipy.linalg import logm
    return logm(m)

def matrix_square_root(m_str):
    m = parse_matrix(m_str)
    from scipy.linalg import sqrtm
    return sqrtm(m)

def polar_decomposition(m_str):
    m = parse_matrix(m_str)
    from scipy.linalg import polar as scipy_polar
    U, P = scipy_polar(m)
    return f"Unitary matrix U:\n{U}\n\nPositive semi-definite matrix P:\n{P}"

def solve_triangular(A_str, b_str):
    A = parse_matrix(A_str)
    b = parse_matrix(b_str)
    from scipy.linalg import solve_triangular
    x = solve_triangular(A, b)
    return x

def polar(m_str):
    """Perform polar decomposition of a matrix (unitary matrix component)."""
    m = parse_matrix(m_str)
    from scipy.linalg import polar as scipy_polar
    U, P = scipy_polar(m)
    return f"Unitary matrix U:\n{U}\n\nPositive semi-definite matrix P:\n{P}"

def generalized_eigen(a_str, b_str):
    """Compute generalized eigenvalues of two matrices."""
    a = parse_matrix(a_str)
    b = parse_matrix(b_str)
    eigvals, _ = scipy.linalg.eig(a, b)
    return eigvals.tolist()

# Aliases to match CLI command names
def lu(m_str):
    return lu_decomposition(m_str)

def qr(m_str):
    return qr_decomposition(m_str)

def cholesky(m_str):
    return cholesky_decomposition(m_str)

def svd(m_str):
    return svd_decomposition(m_str)

def solve(A_str, b_str):
    return solve_linear_system(A_str, b_str)

def exp(m_str):
    return matrix_exponential(m_str)

def sylvester(A_str, B_str, C_str):
    return sylvester_equation(A_str, B_str, C_str)

def power(m_str, n):
    return matrix_power(m_str, n)

def det_via_lu(m_str):
    return determinant_via_lu(m_str)

def inv_via_lu(m_str):
    return inverse_via_lu(m_str)

def log(m_str):
    return matrix_logarithm(m_str)

def sqrt(m_str):
    return matrix_square_root(m_str)
