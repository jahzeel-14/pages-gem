# corazon.py
# Dibuja un corazón rojo usando Python y matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Generamos valores para el parámetro t
t = np.linspace(0, 2 * np.pi, 1000)

# Fórmulas clásicas del corazón
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Configuración del gráfico
plt.figure(figsize=(6, 6))
plt.plot(x, y, color='red', linewidth=2)   # Corazón rojo
plt.fill(x, y, color='red', alpha=0.3)     # Relleno suave
plt.axis('equal')                          # Mantener proporciones
plt.axis('off')                            # Ocultar ejes
plt.title("♥ Corazón en Python ♥", fontsize=16, color='red', pad=20)

# Mostrar el corazón
plt.show()
