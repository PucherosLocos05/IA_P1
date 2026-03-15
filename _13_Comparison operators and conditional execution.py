# Jesus Antonio Baez Ortega 23310372 6E
# LAB#13 Comparison operators and conditional execution

# Solicitamos la entrada del usuario
planta = input("Ingrese la mejor planta del mundo: ")

# Caso 1: Coincidencia exacta (Correcta)
if(planta == "Spathiphyllum"):
    print("Yes - Spathiphyllum is the best plant ever!")

# Caso 2: Coincidencia en minúsculas
elif(planta == "spathiphyllum" ):
    print("No, I want a big Spathiphyllum!")

# Caso 3: Cualquier otra palabra
else: 
    print("Spathiphyllum! Not ", planta + "!")