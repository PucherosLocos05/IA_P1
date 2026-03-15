# Jesus Antonio Baez Ortega 23310372 6E
# LAB#14 Essentials of the if-else statement

# Solicitamos el ingreso anual del usuario
ingreso = float(input("Escriba su ingreso: "))

# Determinamos el impuesto según el nivel de ingresos
if ingreso < 85528:
    # Cálculo para ingresos menores al umbral
    tax = ingreso * 0.18 - 556.02
else:
    # Cálculo para el excedente de ingresos superiores al umbral
    tax = (ingreso - 85528) * 0.32 + 14839.02

# Verificación de seguridad: el impuesto no puede ser menor a cero
if tax < 0.0:
    tax = 0.0

# Redondeamos el resultado final a cero decimales
tax = round(tax, 0)

print("Los impuestos son:", tax, "thalers")