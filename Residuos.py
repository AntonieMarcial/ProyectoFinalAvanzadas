import sys
import sympy as sp
from tkinter import Tk, Label, Entry, Button, Text, END, StringVar, messagebox
import graficar

# --- Variables simbólicas globales ---
z = sp.symbols('z')

# --- Función principal ---
def calcular_integral():
    try:
        # 1) Parsear numerador y denominador
        fz_expr    = sp.sympify(exp_numerador.get(),
                                locals={'pi': sp.pi, 'I': sp.I})
        denom_expr = sp.sympify(exp_denominador.get(),
                                locals={'pi': sp.pi, 'I': sp.I})

        # 2) Resolver polos (raíces del denominador)
        polos = sp.solve(denom_expr, z)

        # 3) Interpretar centro y radio con Sympy (acepta "pi", "I", etc.)
        centro_sym = sp.sympify(centro_input.get(),
                                locals={'pi': sp.pi, 'I': sp.I})
        centro     = complex(float(sp.re(centro_sym)),
                             float(sp.im(centro_sym)))
        radio_sym  = sp.sympify(radio_input.get(), locals={'pi': sp.pi})
        radio      = float(radio_sym)

        # 4) Dibujar el contorno
        graficar.grafica(centro, radio)

        # 5) Clasificar polos dentro/fuera y calcular residuos
        polos_dentro  = []
        polos_fuera   = []
        residuos_all  = {}
        for p in polos:
            # calcular residuo en p con sympy
            resid = sp.simplify(sp.residue(fz_expr/denom_expr, z, p))
            residuos_all[p] = resid

            # clasificar
            if abs(complex(p) - centro) <= radio:
                polos_dentro.append(p)
            else:
                polos_fuera.append(p)

        # 6) Integral = 2πi * suma(residuos en polos dentro)
        if not polos_dentro:
            I_total = 0
        else:
            suma_residuos = sum(residuos_all[p] for p in polos_dentro)
            I_total       = 2 * sp.pi * sp.I * suma_residuos

        # 7) Construir texto de salida
        líneas = []
        líneas.append(f"→ Soluciones : {polos}")
        líneas.append(f"   • Polos dentro del contorno: {polos_dentro}")
        líneas.append(f"   • Polos fuera del contorno:   {polos_fuera}")
        líneas.append("")
        líneas.append("→ Residuos en cada polo:")
        for p, r in residuos_all.items():
            líneas.append(f"     Residuo en z={p}:  {r}")
        líneas.append("")
        líneas.append(f"✔ Aproximación integral = {sp.simplify(I_total)}")

        # 8) Mostrar en el área de texto
        output_text.delete(1.0, END)
        output_text.insert(END, "\n".join(líneas))

    except Exception as e:
        messagebox.showerror("Error en cálculo", str(e))


# --- Construcción de la GUI ---
ventana = Tk()
ventana.title("Calculadora de Residuo y Aproximación Integral")

exp_numerador   = StringVar()
exp_denominador = StringVar()
centro_input    = StringVar()
radio_input     = StringVar()

Label(ventana, text="Numerador f(z):")\
    .grid(row=0, column=0, sticky="e", padx=5, pady=5)
Entry(ventana, textvariable=exp_numerador, width=40)\
    .grid(row=0, column=1, padx=5, pady=5)

Label(ventana, text="Denominador (z - z0)**n:")\
    .grid(row=1, column=0, sticky="e", padx=5, pady=5)
Entry(ventana, textvariable=exp_denominador, width=40)\
    .grid(row=1, column=1, padx=5, pady=5)

Label(ventana, text="Centro del contorno:")\
    .grid(row=2, column=0, sticky="e", padx=5, pady=5)
Entry(ventana, textvariable=centro_input)\
    .grid(row=2, column=1, padx=5, pady=5)

Label(ventana, text="Radio del contorno:")\
    .grid(row=3, column=0, sticky="e", padx=5, pady=5)
Entry(ventana, textvariable=radio_input)\
    .grid(row=3, column=1, padx=5, pady=5)

Button(ventana, text="Evaluar función", command=calcular_integral)\
    .grid(row=4, column=0, columnspan=2, pady=10)

output_text = Text(ventana, height=14, width=70)
output_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()
