# Jesus Antonio Baez Ortega 23310372 6E
# LAB#24 The basics of lists ‒ the Beatles

# Paso 1: Crear lista vacía
beatles = []

# Paso 2: Agregar miembros iniciales
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Paso 3: Pedir nuevos miembros (Stu Sutcliffe y Pete Best)
for i in range(2):
    name = input("Añade miembro a la banda: ")
    beatles.append(name)

# Paso 4: Eliminar a Stu y Pete (posiciones 3 y 4 originalmente)
del beatles[3]
del beatles[3] # El que era 4 ahora es 3

# Paso 5: Insertar a Ringo al inicio de la lista
beatles.insert(0, "Ringo Starr")

print("La alineación final es:", beatles)