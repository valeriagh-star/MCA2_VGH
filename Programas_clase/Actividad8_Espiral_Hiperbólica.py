# --------------------------------
# Autora: García Herrera Valeria
# Fecha: 11 - mayo - 2026
# --------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Constante que controla el tamaño de la espiral
c = 2

# Valores de θ (se evita θ = 0 para no dividir entre cero)
theta = np.linspace(0.1, 10 * np.pi, 1000)

# Ecuación polar de la espiral hiperbólica
r = c / theta

# Crear gráfica en coordenadas polares
plt.figure(figsize=(7, 7))
ax = plt.subplot(111, projection='polar')

# Dibujar la espiral
ax.plot(theta, r, color='darkorange', lw=2, label=r'$r = \frac{c}{\theta}$')
ax.set_title("Espiral Hiperbólica", fontsize=15, pad=25)
ax.grid(True)

plt.legend()
plt.show()
