# Jesus Antonio Baez Ortega 23310372 6E
# LAB#11 Operators and expressions-2

# Solicitamos los datos de entrada como enteros
hours = int(input("Ingrese el numero de horas (0-23): "))
minutes = int(input("Ingrese el numero de minutos (0-59): "))
lasts = int(input("Ingrese la duracion del evento en minutos: "))

# Sumamos la duración a los minutos actuales
minutes = minutes + lasts

# Calculamos el desbordamiento de minutos hacia las horas
# (Por ejemplo, 70 minutos suma 1 hora y quedan 10 minutos)
hours = hours + minutes // 60 

# Aplicamos el módulo para mantener los minutos entre 0 y 59
minutes = minutes % 60 

# Aplicamos el módulo para mantener las horas entre 0 y 23 (formato 24h)
hours = hours % 24 

# Imprimimos el resultado sin espacios adicionales entre los números y los dos puntos
print(hours, ":", minutes, sep='')