import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------
# PROBLEMA 2: Cardioide
# x(t)=a(2cos(t)-cos(2t))
# y(t)=a(2sin(t)-sin(2t))
# ---------------------------------------------------

a = 1

t = np.linspace(0, 2*np.pi, 1000)

x = a*(2*np.cos(t) - np.cos(2*t))
y = a*(2*np.sin(t) - np.sin(2*t))

plt.figure(figsize=(6,6))
plt.plot(x, y, label='Cardioide')

# Rellenar región superior respecto al eje x

t_sup = np.linspace(0, np.pi, 500)
x_sup = a*(2*np.cos(t_sup) - np.cos(2*t_sup))
y_sup = a*(2*np.sin(t_sup) - np.sin(2*t_sup))

plt.fill(x_sup, y_sup, alpha=0.3)

plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.title('Cardioide')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
