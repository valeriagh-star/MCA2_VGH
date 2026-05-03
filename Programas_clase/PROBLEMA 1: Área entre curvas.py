# --------------------------------
# Autora: García Herrera Valeria
# Fecha: 02 - mayo - 2026
# --------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------
# PROBLEMA 1: Área entre curvas
# y = sec^2(x)
# y = 8cos(x)
# x ∈ [-pi/3, pi/3]
# ---------------------------------------------------

x = np.linspace(-np.pi/3, np.pi/3, 1000)

y1 = 1 / (np.cos(x)**2)   # sec^2(x)
y2 = 8 * np.cos(x)

plt.figure(figsize=(8,5))
plt.plot(x, y1, label=r'$y=\sec^2(x)$')
plt.plot(x, y2, label=r'$y=8\cos(x)$')

# sombrear área
plt.fill_between(x, y1, y2, where=(y2 >= y1), alpha=0.3)

plt.title('Área entre curvas')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
