

import numpy as np
import matplotlib.pyplot as plt

# Definición de funciones base
def f(x): return np.sqrt(-x + 0j) # 0j permite manejar raíces de negativos
def g(x): return np.log(x + 0j)    # 0j permite manejar logaritmos de negativos

# Rangos de x ajustados a sus dominios
x_fg = np.linspace(0.01, 1, 400)    # Dominio de f ∘ g: (0, 1]
x_gf = np.linspace(-10, -0.01, 400) # Dominio de g ∘ f: (-inf, 0)
x_prod = np.linspace(-5, 5, 1000)   # Rango para el producto (Dominio Real: Vacío)

plt.figure(figsize=(15, 5))

# 1. Gráfica de la composición f(g(x))
plt.subplot(1, 3, 1)
plt.plot(x_fg, np.real(f(g(x_fg))), color='green', label=r'$f(g(x))$')
plt.title("Composición f ∘ g")
plt.xlabel("x")
plt.grid(True)
plt.legend()

# 2. Gráfica de la composición g(f(x))
plt.subplot(1, 3, 2)
plt.plot(x_gf, np.real(g(f(x_gf))), color='purple', label=r'$g(f(x))$')
plt.title("Composición g ∘ f")
plt.xlabel("x")
plt.grid(True)
plt.legend()

# 3. Gráfica del producto f * g
plt.subplot(1, 3, 3)
# Representación de la componente real del producto; notar que el dominio real es vacío por la intersección de condiciones
plt.plot(x_prod, np.real(f(x_prod) * g(x_prod)), color='blue', linestyle='--', label=r'Re($f \cdot g$)')
plt.axvline(0, color='red', alpha=0.3, label='Sin dominio real')
plt.title("Producto f ⋅ g")
plt.xlabel("x")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
