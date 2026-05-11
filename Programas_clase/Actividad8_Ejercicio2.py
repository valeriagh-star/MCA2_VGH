import numpy as np
import matplotlib.pyplot as plt

# Configuración de la figura
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# -----------------------------------
# 1. Gráfica de x^2 + y^3 - 2y = 3
# -----------------------------------

x = np.linspace(-4, 4, 400)
y = np.linspace(-4, 4, 400)
X, Y = np.meshgrid(x, y)

# Definimos la ecuación implícita f(x, y) = 0
F1 = X**2 + Y**3 - 2*Y - 3

ax1.contour(X, Y, F1, levels=[0], colors='blue')
ax1.set_title(r'$x^2 + y^3 - 2y = 3$')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(True, linestyle='--', alpha=0.6)

# -----------------------------------------------------------
# 2. Ecuación de van der Waals': (P + 5/V^2)(V - 0.03) = 9.7
# -----------------------------------------------------------

# Definimos rangos físicos (V debe ser mayor a 0.03)
v_range = np.linspace(0.04, 2, 400)
p_range = np.linspace(-5, 25, 400)
V, P = np.meshgrid(v_range, p_range)

# Definimos la ecuación implícita f(V, P) = 0
F2 = (P + 5/V**2) * (V - 0.03) - 9.7

ax2.contour(V, P, F2, levels=[0], colors='red')
ax2.set_title('Ecuación de van der Waals')
ax2.set_xlabel('Volumen (V)')
ax2.set_ylabel('Presión (P)')
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
