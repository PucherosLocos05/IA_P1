# Jesus Antonio Baez Ortega 23310372 6E
# LAB#6 Variables ‒ a simple converter

# Definimos las unidades de entrada
kilometers = 12.25
miles = 7.38

# Realizamos los cálculos usando el factor 1.61
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

# Mostramos resultados usando round() para limitar a 2 decimales
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")