from tkinter import Tk, Label, Entry, Button, StringVar
from sympy import symbols, I, factorial, pi, diff, solve, factor, degree
import sys
import graficar

def calcular_integral():
    expression_input = exp_numerador.get()
    numerador_1 = eval(expression_input)
    denominador_input = exp_denominador.get()
    denominador = eval(denominador_input)

    # Resto del código aquí...

# Crear la ventana principal
ventana = Tk()
ventana.title("Calculadora de Integral")

# Variables de entrada
exp_numerador = StringVar()
exp_denominador = StringVar()
centro_input = StringVar()
radio_input = StringVar()

# Función para evaluar la expresión y mostrar resultados
def evaluar_expresion():
    expression_input = exp_numerador.get()
    numerador_1 = eval(expression_input)
    denominador_input = exp_denominador.get()
    denominador = eval(denominador_input)
    centro_value = centro_input.get()
    radio_value = radio_input.get()

    print(f"Numerador: {numerador_1}")
    print(f"Denominador: {denominador}")
    print(f"Centro del contorno: {centro_value}")
    print(f"Radio del contorno: {radio_value}")

# Etiquetas y campos de entrada
Label(ventana, text="Numerador f(z):").grid(row=0, column=0, padx=5, pady=5)
Entry(ventana, textvariable=exp_numerador).grid(row=0, column=1, padx=5, pady=5)

Label(ventana, text="Denominador (z - z0)^(n):").grid(row=1, column=0, padx=5, pady=5)
Entry(ventana, textvariable=exp_denominador).grid(row=1, column=1, padx=5, pady=5)

Label(ventana, text="Centro del contorno:").grid(row=2, column=0, padx=5, pady=5)
Entry(ventana, textvariable=centro_input).grid(row=2, column=1, padx=5, pady=5)

Label(ventana, text="Radio del contorno:").grid(row=3, column=0, padx=5, pady=5)
Entry(ventana, textvariable=radio_input).grid(row=3, column=1, padx=5, pady=5)

# Botón para calcular la integral
Button(ventana, text="Calcular Integral", command=calcular_integral).grid(row=4, column=0, columnspan=2, pady=10)

# Botón para evaluar la expresión
Button(ventana, text="Evaluar Expresión", command=evaluar_expresion).grid(row=5, column=0, columnspan=2, pady=10)

# Ejecutar la interfaz gráfica
ventana.mainloop()
