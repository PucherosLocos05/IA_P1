# Jesus Antonio Baez Ortega 23310372 6E
# LAB#10 Operators and expressions

x = float(input("Ingrese el valor de X: "))

# La clave aquí es el conteo de paréntesis para mantener la jerarquía
# Cada nivel de la fracción está contenido dentro de otro
y = float((1/(x + (1/(x + 1/(x + (1/x)))))))

print("el resultado es: " , y)