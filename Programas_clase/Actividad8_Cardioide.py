# --------------------------------
# Autora: García Herrera Valeria
# Fecha: 11 - mayo - 2026
# --------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Parámetro que controla el tamaño de la cardioide
a = 2

# Valores de θ en el intervalo [0, 2π]
theta = np.linspace(0, 2 * np.pi, 1000)

# Ecuación polar: r(θ) = a(1 + cos(θ))
r = a * (1 + np.cos(theta))

# Conversión de coordenadas polares a cartesianas
x = r * np.cos(theta)
y = r * np.sin(theta)

# Configuración de la gráfica
plt.figure(figsize=(7, 7))

# Dibujar la cardioide
plt.plot(x, y, color='deeppink', linewidth=2, label=r'$r = a(1+\cos(\theta))$')

plt.title('Gráfica de una Cardioide', fontsize=14)
plt.xlabel('x')
plt.ylabel('y')

# Ejes coordenados
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Cuadrícula y escala uniforme
plt.grid(True, linestyle='--', alpha=0.6)
plt.axis('equal')
plt.legend()
plt.show()
