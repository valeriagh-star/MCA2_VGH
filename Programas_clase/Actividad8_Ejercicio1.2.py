# --------------------------------
# Autora: García Herrera Valeria
# Fecha: 11 - mayo - 2026
# --------------------------------

import numpy as np
import matplotlib.pyplot as plt

def chang_function(x, derivative=0):
    total = np.zeros_like(x)
    for k in range(1, 101):
        if derivative == 0:
            total += (np.sin(2 * np.pi * k**2 * x) / (4 * np.pi**2 * k**5)) + (x**2 / (2 * k))
        elif derivative == 1:
            total += (np.cos(2 * np.pi * k**2 * x) / (2 * np.pi * k**3)) + (x / k)
        elif derivative == 2:
            total += -k * np.sin(2 * np.pi * k**2 * x) + (1 / k)
    return total

# Se utilizan 5000 puntos para una mejor resolución de las oscilaciones de alta frecuencia
x = np.linspace(-1, 1, 5000) 

fig, axs = plt.subplots(3, 1, figsize=(10, 12))

# Función Original f(x)
axs[0].plot(x, chang_function(x, 0), 'b')
axs[0].set_title(r"Función Original $f(x)$ (Comportamiento visualmente suave)")

# Primera Derivada f'(x)
axs[1].plot(x, chang_function(x, 1), 'g')
axs[1].set_title(r"Primera Derivada $f'(x)$ (Inicio de inestabilidad oscilatoria)")

# Segunda Derivada f''(x)
axs[2].plot(x, chang_function(x, 2), 'r', lw=0.5)
axs[2].set_title(r"Segunda Derivada $f''(x)$ (Oscilaciones de alta frecuencia y amplitud creciente)")

for ax in axs: ax.grid(True)
plt.tight_layout()
plt.show()
