# Jesus Antonio Baez Ortega 23310372 6E
# LAB#27 How many days: writing and using your own functions

def is_year_leap(year):
    # Función auxiliar: determina si el año es bisiesto
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    # Paso 1: Validación de datos de entrada
    if year < 1 or month < 1 or month > 12:
        return None
    
    # Paso 2: Definición de días por mes (año común)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Paso 3: Caso especial - Febrero en año bisiesto
    if month == 2 and is_year_leap(year):
        return 29
    
    # Paso 4: Retorno del valor usando el índice (mes - 1)
    return month_days[month - 1]

# --- Testing Code ---
# Aquí verificamos casos críticos: años bisiestos, comunes y meses inválidos