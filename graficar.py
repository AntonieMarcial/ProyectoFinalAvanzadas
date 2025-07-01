import matplotlib.pyplot as plt
import numpy as np

def grafica(centro, radio, puntos_dentro=None, puntos_fuera=None):
   
    theta = np.linspace(0, 2*np.pi, 100)

    # Calcular las coordenadas del círculo en el plano complejo
    x = centro.real + radio * np.cos(theta)
    y = centro.imag + radio * np.sin(theta)

    # Graficar el círculo
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label='Círculo en el plano complejo')

    # Marcar el centro
    plt.scatter(centro.real, centro.imag, color='green', label='Centro')

    # Configurar el aspecto del gráfico
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    # Graficar los puntos dentro del círculo (en azul)
    if puntos_dentro is not None:
        x_dentro = [p.real for p in puntos_dentro]
        y_dentro = [p.imag for p in puntos_dentro]
        plt.scatter(x_dentro, y_dentro, color='blue', marker='o', label='Puntos dentro del círculo')

    # Graficar los puntos fuera del círculo (en rojo)
    if puntos_fuera is not None:
        x_fuera = [p.real for p in puntos_fuera]
        y_fuera = [p.imag for p in puntos_fuera]
        plt.scatter(x_fuera, y_fuera, color='red', marker='x', label='Puntos fuera del círculo')

    # Añadir etiquetas y leyenda
    plt.title('Círculo en el plano complejo')
    plt.xlabel('Eje Real')
    plt.ylabel('Eje Imaginario')
    plt.legend()

    plt.savefig('circulo_en_plano_complejo.png')
    # Mostrar el gráfico
    plt.show()