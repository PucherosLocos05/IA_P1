# Jesus Antonio Baez Ortega 23310372 6E
# LAB#15 Essentials of the if-elif-else statement

year = int(input("Ingrese el año: "))

# Verificamos si el año pertenece a la era del calendario gregoriano
if year < 1582:
    print("El año no esta dentro del calendario gregoriano")
else:
    # Si no es divisible entre 4, es un año común
    if year % 4 != 0:
        print(year, "es un año comun")
    # Si es divisible entre 4 pero no entre 100, es bisiesto
    elif year % 100 != 0:
        print(year, "es un año bisiesto")
    # Si es divisible entre 100 pero no entre 400, es común
    elif year % 400 != 0:
        print(year, "es un año comun")
    # Si es divisible entre 400, es bisiesto
    else:
        print(year, "es un año bisiesto")