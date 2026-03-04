#Jesus Antonio Baez Ortega 23310372 6E
#LAB#15 Essentials of the if-elif-else statement

year = int(input("Ingrese el año: "))

if year < 1582:
    print("El año no esta dentro del calendario gregoriano")
else:
    if year % 4 != 0:
        print(year , " es un año comun")
    elif year % 100 != 0:
        print(year , " es un año bisiesto")
    elif year % 400 != 0:
        print(year , "es un año comun")
    else:
        print(year , " es un año bisiesto")