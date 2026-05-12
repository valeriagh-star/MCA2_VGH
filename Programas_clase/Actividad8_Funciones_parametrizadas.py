# --------------------------------
# Autora: García Herrera Valeria
# Fecha: 11 - mayo - 2026
# --------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Definimos el parámetro t en el rango especificado: 0 <= t <= 14π
# Usamos muchos puntos (1000) para que la curva se vea suave
t = np.linspace(0, 14 * np.pi, 1000)

# Definición de las funciones paramétricas x(t) e y(t)
x = np.cos(t) + (1/2) * np.cos(7 * t) + (1/3) * np.sin(17 * t)
y = np.sin(t) + (1/2) * np.sin(7 * t) + (1/3) * np.cos(17 * t)

# Configuración de la gráfica
plt.figure(figsize=(8, 8))
plt.plot(x, y, color='darkcyan', lw=1.5)

plt.title(r'Gráfica de funciones parametrizadas ($0 \leq t \leq 14\pi$)', fontsize=14)
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.axis('equal') # Mantiene la proporción para no deformar la figura
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
