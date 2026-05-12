# --------------------------------
# Autora: García Herrera Valeria
# Fecha: 11 - mayo - 2026
# --------------------------------

# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Justificación de la conducta observada:
# La variación del parámetro h modifica la frecuencia de oscilación de la función armónica cos(hθ).
# Al aumentar h, la función completa más ciclos en el intervalo de 0 a 2π, generando un mayor número de pétalos en la gráfica.
# Se observa que cuando h es par, la curva presenta 2h pétalos, ya que los valores negativos de la función coseno producen pétalos adicionales
# que no se sobreponen. En cambio, cuando h es impar, dichos pétalos se superponen debido a la simetría de la curva polar,
# por lo que únicamente se distinguen h pétalos.
# ----------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Valores de h solicitados
valores_h = [1, 2, 3, 4, 5, 6]

fig, axes = plt.subplots(1, 6, figsize=(22, 4))

theta = np.linspace(0, 2 * np.pi, 5000)

for i, h in enumerate(valores_h):

    r = 3 * np.cos(h * theta)

    # Conversión polar → cartesiana
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    axes[i].plot(x, y, color='tab:blue', lw=2)

    axes[i].set_title(f'h = {h}', fontsize=14, fontweight='bold')
    axes[i].axis('off')
    axes[i].axis('equal')

plt.tight_layout()
plt.show()
