# Jesus Antonio Baez Ortega 23310372 6E
# LAB#21 Essentials of the while loop

blocks = int(input("Ingrese el número de bloques: "))

height = 0
layer = 1 # Representa el número de bloques necesarios para el nivel actual

# Mientras los bloques que tenemos alcancen para completar el siguiente nivel
while blocks >= layer:
    blocks -= layer  # Restamos los bloques usados
    height += 1      # Aumentamos la altura lograda
    layer += 1       # El siguiente nivel requerirá un bloque más que el anterior

print("La altura de la piramide es:", height)