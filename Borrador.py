import tkinter as tk
from sympy import symbols, I, factorial, pi, diff, solve, factor, degree
import graficar

def punto_dentro_del_contorno(punto, centro, radio):
    distancia_al_centro = abs(punto - centro)
    return distancia_al_centro <= radio

def calcular_integral():
    numerador_1 = entry_numerador.get()
    denominador_input = entry_denominador.get()

    z, n = symbols('z n', complex=True)
    numerador = eval(numerador_1.replace('pi', str(pi)))
    denominador = eval(denominador_input.replace('pi', str(pi)))

    z_values = solve(denominador, z)

    if denominador.is_polynomial(z):
        denominador_factorizado = factor(denominador)
        factores = denominador_factorizado.as_ordered_factors()
        cantidad_de_factores = len(factores)
        exponente_mayor_grado = max(degree(f, z) for f in factores)
        print(f"Exponente de mayor grado en el denominador factorizado es: {exponente_mayor_grado}")
    else:
        print("El denominador no es un polinomio.")

    print(f"La factorización del denominador es: {denominador_factorizado}")

    centro_input = eval(entry_centro.get())
    radio_input = eval(entry_radio.get())
    
    factores_dentro_del_contorno = []
    graficar.grafica(centro_input, radio_input)

    for i, factor_i in enumerate(factores):
        if abs(factor_i.subs(z, centro_input)) <= radio_input:
            factores_dentro_del_contorno.append(factor_i)
        else:
            fz = numerador / factor_i
            print(f"fz para Factor_{i+1} fuera del contorno: {fz}")

    valores_z0_dentro_del_contorno = []
    puntos_dentro = []
    puntos_fuera = []

    print(f"Las soluciones para z0 son: {z_values}")

    for i, factor_i in enumerate(factores):
        print(f"Factor_{i+1}:", factor_i)

    if cantidad_de_factores == 1:
        for z_value in z_values: 
            if punto_dentro_del_contorno(z_value, centro_input, radio_input):
                valores_z0_dentro_del_contorno.append(z_value)
                derivada_n_z0_value = diff(numerador, z, (exponente_mayor_grado-1)).subs(z, z_value)
                factorial_n = factorial((exponente_mayor_grado-1))
                integral_result_per_z = (derivada_n_z0_value / factorial_n) * 2 * pi * I

                if (exponente_mayor_grado == 1):
                    fz_evaluada = numerador.subs(z, z_value)
                    integral_result_per_z = fz_evaluada * 2 * pi * I

                print("Valores de z0 dentro del contorno:", valores_z0_dentro_del_contorno)        
        if not valores_z0_dentro_del_contorno:
            print("La función es analítica en todos los puntos dentro o sobre el contorno. La integral es 0.")
            return

        print(f"La {exponente_mayor_grado-1}-ésima derivada de {numerador} en z = {valores_z0_dentro_del_contorno} es: {derivada_n_z0_value}")
        print(f"La integral despejada de la función ({numerador}/ {denominador_input}) =  {integral_result_per_z}")
        
    else:
        for z_value in z_values: 
            if punto_dentro_del_contorno(z_value, centro_input, radio_input):
                valores_z0_dentro_del_contorno.append(z_value)
                fz = numerador / factor_i
                derivada_n_z0_value = diff(fz, z, (exponente_mayor_grado-1)).subs(z, z_value)
                factorial_n = factorial((exponente_mayor_grado-1))
                integral_result_per_z = (derivada_n_z0_value / factorial_n) * 2 * pi * I
        
                if (exponente_mayor_grado == 1):
                    fz_evaluada = fz.subs(z, z_value)
                    integral_result_per_z = fz_evaluada * 2 * pi * I

                print("Valores de z0 dentro del contorno:", valores_z0_dentro_del_contorno)     
        if not valores_z0_dentro_del_contorno:
            print("La función es analítica en todos los puntos dentro o sobre el contorno. La integral es 0.")
            return

        print(f"La {exponente_mayor_grado-1}-ésima derivada de {fz} en z = {valores_z0_dentro_del_contorno} es: {derivada_n_z0_value}")
        print(f"La integral despejada de la función ({fz}/ {factores_dentro_del_contorno}) =  {integral_result_per_z}")
        print("Valores de z0 dentro del contorno:", valores_z0_dentro_del_contorno)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Integral")

# Crear y posicionar los elementos en la ventana
label_numerador = tk.Label(ventana, text="Numerador f(z):")
label_numerador.pack()

entry_numerador = tk.Entry(ventana)
entry_numerador.pack()

label_denominador = tk.Label(ventana, text="Denominador (z - z0)^(n):")
label_denominador.pack()

entry_denominador = tk.Entry(ventana)
entry_denominador.pack()

label_centro = tk.Label(ventana, text="Centro del contorno:")
label_centro.pack()

entry_centro = tk.Entry(ventana)
entry_centro.pack()

label_radio = tk.Label(ventana, text="Radio del contorno:")
label_radio.pack()

entry_radio = tk.Entry(ventana)
entry_radio.pack()

boton_calcular = tk.Button(ventana, text="Calcular Integral", command=calcular_integral)
boton_calcular.pack()

# Iniciar el bucle principal
ventana.mainloop()
