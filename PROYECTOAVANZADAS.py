from sympy import symbols, I, factorial, pi, diff, solve, factor, degree, exp, sin, cos, tan, cot, sec, csc, coth, csch,sinh,cosh,tanh,sech
import sys
import graficar
# Definir variables simbólicas
z, n = symbols('z n', complex=True)
print(f"Ingrese I cuando se refiera a i compleja e ingrese pi cuando se refiera al valor de pi ")
# Permitir que el usuario ingrese la función analítica X = f(z)/(z - z0)^(n+1)
expression_input = input("Ingrese el numerador f(z) de la función analítica  en términos de 'z': ")
numerador_1 = eval(expression_input)
expression_input = expression_input.replace('pi', str(pi))

# Permitir que el usuario ingrese el denominador 
denominador_input = input("Ingrese el denominador (z - z0)^(n) en términos de 'z': ")
denominador = eval(denominador_input)
denominador_input = denominador_input.replace('pi', str(pi))
# Despejar z del denominador
z_values = solve(denominador, z)

# Factorizar el denominador y obtener el exponente de mayor grado
if denominador.is_polynomial(z):
    denominador_factorizado = factor(denominador)
    # Obtener los factores
    factores = denominador_factorizado.as_ordered_factors()
    cantidad_de_factores = len(factores)
   # Guardar cada factor en una variable
    for i, factor_i in enumerate(factores):
        globals()[f'factor_{i+1}'] = factor_i
    # Buscar el mayor exponente entre los factores
    exponente_mayor_grado = max(degree(f, z) for f in factores)
    print(f"Exponente de mayor grado en el denominador factorizado es: {exponente_mayor_grado}")
else:
    print("El denominador no es un polinomio.")

print(f"La factorización del denominador es: {denominador_factorizado}")

# Permitir que el usuario ingrese el centro
centro_input = eval(input("Ingrese el valor para el centro del contorno: "))
try:
    centro_input_1 = complex(centro_input)
except ValueError:
    print("Error: Ingresa un valor válido para el centro.")
    sys.exit()
# Permitir que el usuario ingrese el radio
radio_input = eval(input("Ingrese el valor para el radio del contorno: "))
# Lista para almacenar los factores dentro del contorno
factores_dentro_del_contorno = []
graficar.grafica (centro_input_1,radio_input)
# Seleccionar factores dentro del contorno
for i, factor_i in enumerate(factores):
    # Evaluar el factor en el centro y verificar si está dentro del contorno
    if abs(factor_i.subs(z, centro_input)) <= radio_input:
        factores_dentro_del_contorno.append(factor_i)
    else:
        # Definir fz para factores fuera del contorno
        fz = numerador_1 / factor_i
        print(f"fz para Factor_{i+1} fuera del contorno: {fz}")

# Función para verificar si un punto está dentro del contorno
def punto_dentro_del_contorno(punto, centro, radio):
    distancia_al_centro = abs(punto - centro)
    return distancia_al_centro <= radio

# Lista para almacenar los valores de z0 dentro del contorno
valores_z0_dentro_del_contorno = []
puntos_dentro = []
puntos_fuera = []
# Mostrar las soluciones para z0
print(f"Las soluciones para z0 son: {z_values}")

for i, factor_i in enumerate(factores):
        print(f"Factor_{i+1}:", factor_i)

if cantidad_de_factores == 1:
    for z_value in z_values: 
        if punto_dentro_del_contorno(z_value, centro_input, radio_input):
            valores_z0_dentro_del_contorno.append(z_value)
            derivada_n_z0_value = diff(numerador_1, z, (exponente_mayor_grado-1)).subs(z, z_value)

            # Calcular el factorial de n
            factorial_n = factorial((exponente_mayor_grado-1))

            # Calcular la integral despejada 
            integral_result_per_z = (derivada_n_z0_value / factorial_n) * 2 * pi * I
            if (exponente_mayor_grado ==1) :
                fz_evaluada = numerador_1.subs(z,z_value)
                integral_result_per_z = fz_evaluada * 2 * pi * I
            print("Valores de z0 dentro del contorno:", valores_z0_dentro_del_contorno)        
    if not valores_z0_dentro_del_contorno:
        # No hay valores dentro del contorno
        print("La función es analítica en todos los puntos dentro o sobre el contorno. La integral es 0.")
        sys.exit()
    print(f"La {exponente_mayor_grado-1}-ésima derivada de {numerador_1} en z = {valores_z0_dentro_del_contorno} es: {derivada_n_z0_value}")
    print(f"La integral despejada de la función ({numerador_1}/ {denominador_input}) =  {integral_result_per_z}")
    
else :            
# Calcular la derivada en z0 y verificar si está dentro del contorno
    for z_value in z_values: 
        if punto_dentro_del_contorno(z_value, centro_input, radio_input):
            valores_z0_dentro_del_contorno.append(z_value)
            derivada_n_z0_value = diff(fz, z, (exponente_mayor_grado-1)).subs(z, z_value)

            # Calcular el factorial de n
            factorial_n = factorial((exponente_mayor_grado-1))

            # Calcular la integral despejada utilizando la fórmula integral de Cauchy
            integral_result_per_z = (derivada_n_z0_value / factorial_n) * 2 * pi * I
    
            if (exponente_mayor_grado ==1) :
                 fz_evaluada = fz.subss(z,z_value)
                 integral_result_per_z = fz_evaluada * 2 * pi * I
            print("Valores de z0 dentro del contorno:", valores_z0_dentro_del_contorno)     
    if not valores_z0_dentro_del_contorno:
        # No hay valores dentro del contorno
        print("La función es analítica en todos los puntos dentro o sobre el contorno. La integral es 0.")
        sys.exit()        
    print(f"La {exponente_mayor_grado-1}-ésima derivada de {fz} en z = {valores_z0_dentro_del_contorno} es: {derivada_n_z0_value}")
    print(f"La integral despejada de la función ({fz}/ {factores_dentro_del_contorno}) =  {integral_result_per_z}")



