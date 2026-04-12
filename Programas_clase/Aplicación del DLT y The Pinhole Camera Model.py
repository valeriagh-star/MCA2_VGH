# --------------------------------
# Autora: García Herrera Valeria
# Fecha: 06 - marzo - 2026
# --------------------------------

import numpy as np

# ---------------------------
# 1. Puntos 3D (en cm)
# ---------------------------

M = np.array([
    [0,0,0,1],
    [26.3,0,0,1],
    [26.3,19.6,0,1],
    [0,0,11.3,1],
    [26.3,0,11.3,1],
    [26.3,19.6,11.3,1]
])

# ---------------------------
# 2. Puntos 2D (en pixeles)
# ---------------------------

m = np.array([
    [852, 1583],
    [2459,1500],
    [2788,1166],
    [983,1083],
    [2376,1033],
    [2624,833]
])

# --------------------------------
# 3. Construcción de la matriz A
# --------------------------------

A = []

for i in range(len(M)):
    X, Y, Z, W = M[i]
    u, v = m[i]

    A.append([X, Y, Z, W, 0, 0, 0, 0, -u*X, -u*Y, -u*Z, -u])
    A.append([0, 0, 0, 0, X, Y, Z, W, -v*X, -v*Y, -v*Z, -v])

A = np.array(A)

# ------------
# 4. SVD
# ------------

U, S, Vt = np.linalg.svd(A)

# Última fila de V^T

p = Vt[-1]

# -----------------
# 5. Matriz P
# -----------------

P = p.reshape(3,4)

print("Vector p:\n", p)
print("\nMatriz P:\n", P)

# ---------------------
# 6. Verificación
# ---------------------

print("\nVerificación de reproyección:\n")

error_total = 0

for i in range(len(M)):
    proj = P @ M[i]
    proj = proj / proj[2]  # normalización

    u_est, v_est = proj[0], proj[1]
    u_real, v_real = m[i]

    error = np.sqrt((u_est - u_real)**2 + (v_est - v_real)**2)
    error_total += error

    print(f"Punto {i+1}:")
    print(f" Real: ({u_real:.2f}, {v_real:.2f})")
    print(f" Estimado: ({u_est:.2f}, {v_est:.2f})")
    print(f" Error: {error:.2f} pixeles\n")

print("Error promedio:", error_total / len(M))
