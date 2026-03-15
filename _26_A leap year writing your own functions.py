# Jesus Antonio Baez Ortega 23310372 6E
# LAB#26 A leap year: writing your own functions

def is_year_leap(year):
    # La lógica sigue la jerarquía del calendario gregoriano
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True   # Divisible entre 400 -> Bisiesto
            else:
                return False  # Siglo no divisible entre 400 -> Común
        else:
            return True       # Divisible entre 4 pero no entre 100 -> Bisiesto
    else:
        return False          # No divisible entre 4 -> Común

# --- Código de Prueba (Testing) ---
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "-> ", end="")
    result = is_year_leap(yr)
    
    # Comparamos el retorno de la función con nuestro resultado esperado
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")