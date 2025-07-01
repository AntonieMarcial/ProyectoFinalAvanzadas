import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

def grafica(centro, radio, puntos_z0, puntos_z1):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = centro.real + radio * np.cos(theta)
    y = centro.imag + radio * np.sin(theta)

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label='Círculo en el plano complejo')
    plt.scatter(centro.real, centro.imag, color='red', label='Centro')

    # Marcar puntos z0 y z1
    if puntos_z0:
        for punto in puntos_z0:
            plt.scatter(punto.real, punto.imag, color='blue', label='Punto z0')
    if puntos_z1:
        for punto in puntos_z1:
            plt.scatter(punto.real, punto.imag, color='grey', label='Punto z1')

    # Otras configuraciones de la gráfica...

    # Guardar la imagen
    if not os.path.exists('graficos'):
        os.makedirs('graficos')
    filename = f'graficos/grafico_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
    plt.savefig(filename)
    plt.show()

    return filename