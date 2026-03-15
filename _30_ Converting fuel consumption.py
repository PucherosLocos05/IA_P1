#Jesus Antonio Baez Ortega 23310372 6E
#LAB#30  Converting fuel consumption
def liters_100km_to_miles_gallon(liters):
    # 100 km converted to miles
    miles = 100 / 1.609344
    # liters converted to gallons
    gallons = liters / 3.785411784
    return miles / gallons

def miles_gallon_to_liters_100km(mpg):
    # 1 gallon converted to liters
    liters = 3.785411784
    # mpg converted to km (miles * 1.609344)
    km = mpg * 1.609344
    # We need liters per 100km, so: (liters / km) * 100
    return (liters / km) * 100

# Testing the functions
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))