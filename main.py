import tkinter as tk
from integrador import integrar
from Graficador import grafica

# Función para manejar la integración y graficación
def handle_integration():
    numerador = numerador_input.get()
    denominador = denominador_input.get()
    centro = centro_input.get()
    radio = radio_input.get()

    # Llamar a la función de integración y manejar los resultados
    resultado_integracion = integrar(numerador, denominador, centro, radio)
    if "error" in resultado_integracion:
        resultado_label.config(text=f"Error: {resultado_integracion['error']}")
    else:
        # Aquí se pueden agregar más detalles del resultado si es necesario
        resultado_label.config(text=f"Resultado: {resultado_integracion['resultado']}")

        # Obtener los puntos z0 y z1 para la graficación
        puntos_z0 = resultado_integracion.get("valores_z0", [])
        puntos_z1 = []  # Asumiendo que tienes alguna lógica para determinar puntos z1

        # Llamar a la función del graficador
        grafica(complex(eval(centro)), eval(radio), puntos_z0, puntos_z1)

# Crear la ventana principal
root = tk.Tk()
root.title("Integrador de Contornos Complejos")

# Crear y configurar la interfaz
# Numerador
numerador_label = tk.Label(root, text="Numerador:")
numerador_label.grid(row=0, column=0)
numerador_input = tk.Entry(root)
numerador_input.grid(row=0, column=1)

# Denominador
denominador_label = tk.Label(root, text="Denominador:")
denominador_label.grid(row=1, column=0)
denominador_input = tk.Entry(root)
denominador_input.grid(row=1, column=1)

# Centro
centro_label = tk.Label(root, text="Centro:")
centro_label.grid(row=2, column=0)
centro_input = tk.Entry(root)
centro_input.grid(row=2, column=1)

# Radio
radio_label = tk.Label(root, text="Radio:")
radio_label.grid(row=3, column=0)
radio_input = tk.Entry(root)
radio_input.grid(row=3, column=1)

# Botón de integración
integrar_button = tk.Button(root, text="Integrar", command=handle_integration)
integrar_button.grid(row=4, column=1)

# Etiqueta para mostrar resultados
resultado_label = tk.Label(root, text="Resultado aparecerá aquí")
resultado_label.grid(row=5, column=1, columnspan=2)

# Iniciar el bucle principal de Tkinter
root.mainloop()