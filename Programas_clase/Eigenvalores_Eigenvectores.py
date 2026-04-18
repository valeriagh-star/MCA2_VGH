

from sympy import Matrix, Rational
import numpy as np

# ====================================
# INCISO A) Matriz de Hilbert 3x3
# ====================================

print("\n" + "="*20 + " INCISO A " + "="*20)

# 1.- Cálculo con numpy
A1_a = np.array([[1, 1/2, 1/3], [1/2, 1/3, 1/4], [1/3, 1/4, 1/5]])
eigenvalores_a, eigenvectores_a = np.linalg.eig(A1_a)
print("\nEigenvalores y Eigenvectores con numpy \n")
print("Eigenvalores:\n", eigenvalores_a)
print("Eigenvectores unitarios:\n", eigenvectores_a)

# 2.- Cálculo con sympy
A2_a = Matrix([[1, Rational(1,2), Rational(1,3)], 
               [Rational(1,2), Rational(1,3), Rational(1,4)], 
               [Rational(1,3), Rational(1,4), Rational(1,5)]])
eigen_data_a = A2_a.eigenvects()

print("\nEigenvalores y Eigenvectores (en formato 'exacto') con sympy ")
for i, (val, mult, vecs) in enumerate(eigen_data_a):
    print(f"\nEl Eigenvalor {i+1} es: {val}")
    for j, vec in enumerate(vecs):
        print(f"   Un eigenvector de {val} es: {vec.tolist()}")

print("\nMatriz P de eigenvectores: ")
P_a = A2_a.eigenvects()[0][2][0].row_join(A2_a.eigenvects()[1][2][0]).row_join(A2_a.eigenvects()[2][2][0])
print("P = ", P_a.tolist())


# =======================================
# INCISO B) Matriz de Vandermonde 4x4
# =======================================

print("\n\n" + "="*20 + " INCISO B " + "="*20)

# 1.- Cálculo con numpy
A1_b = np.array([
    [1**0, 1**0, 1**0, 1**0],
    [1.01, 1.02, 1.03, 1.04],
    [1.01**2, 1.02**2, 1.03**2, 1.04**2],
    [1.01**3, 1.02**3, 1.03**3, 1.04**3]
])
eigenvalores_b, eigenvectores_b = np.linalg.eig(A1_b)
print("\nEigenvalores y Eigenvectores con numpy \n")
print("Eigenvalores:\n", eigenvalores_b)
print("Eigenvectores unitarios:\n", eigenvectores_b)

# 2.- Cálculo con sympy
A2_b = Matrix(A1_b.tolist())
eigen_data_b = A2_b.eigenvects()

print("\nEigenvalores y Eigenvectores (en formato 'exacto') con sympy ")
for i, (val, mult, vecs) in enumerate(eigen_data_b):
    print(f"\nEl Eigenvalor {i+1} es: {val}")
    for j, vec in enumerate(vecs):
        print(f"   Un eigenvector de {val} es: {vec.tolist()}")

print("\nMatriz P de eigenvectores: ")
P_b = A2_b.eigenvects()[0][2][0]
for k in range(1, len(A2_b.eigenvects())):
    P_b = P_b.row_join(A2_b.eigenvects()[k][2][0])
print("P = ", P_b.tolist())


# ===========================
# INCISO C) Matriz 2x2 
# ===========================

print("\n\n" + "="*20 + " INCISO C " + "="*20)

# 1.- Cálculo con numpy
A1_c = np.array([[1, 2], [2, 4.0001]])
eigenvalores_c, eigenvectores_c = np.linalg.eig(A1_c)
print("\nEigenvalores y Eigenvectores con numpy \n")
print("Eigenvalores:\n", eigenvalores_c)
print("Eigenvectores unitarios:\n", eigenvectores_c)

# 2.- Cálculo con sympy
A2_c = Matrix([[1, 2], [2, Rational(40001, 10000)]])
eigen_data_c = A2_c.eigenvects()

print("\nEigenvalores y Eigenvectores (en formato 'exacto') con sympy ")
for i, (val, mult, vecs) in enumerate(eigen_data_c):
    print(f"\nEl Eigenvalor {i+1} es: {val}")
    for j, vec in enumerate(vecs):
        print(f"   Un eigenvector de {val} es: {vec.tolist()}")

print("\nMatriz P de eigenvectores: ")
P_c = A2_c.eigenvects()[0][2][0].row_join(A2_c.eigenvects()[1][2][0])
print("P = ", P_c.tolist())
