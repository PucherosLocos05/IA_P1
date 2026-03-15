# Jesus Antonio Baez Ortega 23310372 6E
# LAB#23 The basics of lists

# Lista inicial: 5 elementos
hat_list = [1, 2, 3, 4, 5]

# Paso 1: El usuario reemplaza el número central (índice 2)
hat_list[2] = int(input("Ingresa un número para el centro: "))

# Paso 2: Eliminamos el último elemento usando el índice negativo
del hat_list[-1]

# Paso 3: Medimos la nueva longitud de la lista (ahora será 4)
print("Longitud de la lista:", len(hat_list))

# Imprimimos el estado final de la lista
print("Contenido final:", hat_list)