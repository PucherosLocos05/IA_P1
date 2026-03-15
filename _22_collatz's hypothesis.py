# Jesus Antonio Baez Ortega 23310372 6E
# LAB#22 Collatz's hypothesis

c0 = int(input("Ingrese un número entero positivo: "))
steps = 0

# El bucle continúa hasta que el número se convierte en 1
while c0 != 1:
    if c0 % 2 == 0:
        # Si es par, aplicamos división entera
        c0 = c0 // 2
    else:
        # Si es impar, aplicamos la fórmula 3n + 1
        c0 = 3 * c0 + 1
    
    print(c0)      # Imprimimos cada valor de la secuencia
    steps += 1     # Contamos cada iteración

print("pasos =", steps)