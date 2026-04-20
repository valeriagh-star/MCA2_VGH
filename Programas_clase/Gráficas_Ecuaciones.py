# ===================================
# Autora: García Herrera Valeria
# Fecha: 19 - abril - 2026
# ===================================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ===================================
# INCISO A: Matriz de Hilbert 3x3
# ===================================

A = np.array([[1, 1/2, 1/3],
              [1/2, 1/3, 1/4],
              [1/3, 1/4, 1/5]])

# Gráfica 3D (Planos)
fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(121, projection='3d')
x_range = np.linspace(-2, 2, 10)
y_range = np.linspace(-2, 2, 10)
X, Y = np.meshgrid(x_range, y_range)

# Despeje de Z de cada ecuación (Ax = b, con b=[1, 0, 0])
Z1 = (1 - X - 0.5*Y) * 3
Z2 = (-0.5*X - (1/3)*Y) * 4
Z3 = (-(1/3)*X - 0.25*Y) * 5

ax1.plot_surface(X, Y, Z1, alpha=0.3, color='blue')
ax1.plot_surface(X, Y, Z2, alpha=0.3, color='red')
ax1.plot_surface(X, Y, Z3, alpha=0.3, color='green')
ax1.set_title("Planos Inciso A (Matriz de Hilbert)")

# ======================================
# INCISO C: Matriz Casi Singular 2x2
# ======================================

C = np.array([[1, 2],
              [2, 4.0001]])

# Gráfica 2D (Líneas)
ax2 = fig.add_subplot(122)
x_vals = np.linspace(0, 5, 100)
# Despejes: y = (b - ax) / c
y1_c = (3 - x_vals) / 2
y2_c = (6.0001 - 2*x_vals) / 4.0001

ax2.plot(x_vals, y1_c, 'b-', label='x + 2y = 3')
ax2.plot(x_vals, y2_c, 'r--', label='2x + 4.0001y = 6.0001')
ax2.set_title("Líneas Inciso C (Casi paralelas)")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()
