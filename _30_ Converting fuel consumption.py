# Jesus Antonio Baez Ortega 23310372 6E
# LAB#30 Converting fuel consumption

def liters_100km_to_miles_gallon(liters):
    # Convertimos la distancia fija (100km) a millas
    miles = 100 / 1.609344
    # Convertimos el volumen consumido a galones
    gallons = liters / 3.785411784
    return miles / gallons

def miles_gallon_to_liters_100km(mpg):
    # Definimos el volumen de 1 galón en litros
    liters = 3.785411784
    # Convertimos la distancia recorrida (millas) a kilómetros
    km = mpg * 1.609344
    # Calculamos cuántos litros se gastan por cada 100km
    return (liters / km) * 100

# Pruebas de salida
# Un valor bajo en L/100km (3.9) debe dar un valor alto en MPG (~60.3)
print(liters_100km_to_miles_gallon(3.9)) 
print(miles_gallon_to_liters_100km(60.3))