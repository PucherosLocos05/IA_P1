#Jesus Antonio Baez Ortega 23310372 6E
#LAB#14 Essentials of the if-else statement
ingreso = float(input("Escriba su ingreso "))

if ingreso < 85528:
   tax = ingreso * 0.18 - 556.02
else:
   tax = (ingreso - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("los impuestos :", tax, "thalers")