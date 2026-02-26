#Jesus Antonio Baez Ortega 23310372 6E
#LAB#11 Operators and expressions-2
hours = int(input("Ingrese el numero de horas (1-23)"))
minutes = int(input("Ingrese el numero de minutos(1-59)"))
lasts = int(input("Ingrese la duracion del evento"))

minutes = minutes + lasts
hours = hours + minutes // 60 
minutes = minutes % 60 
hours = hours % 24 
print(hours, ":", minutes, sep='')
