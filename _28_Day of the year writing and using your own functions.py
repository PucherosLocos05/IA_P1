# Jesus Antonio Baez Ortega 23310372 6E
# LAB#28 Day of the year: writing and using your own functions

def is_year_leap(year):
    # Nivel 1: Lógica base (Bisiestos)
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    # Nivel 2: Depende del Nivel 1 para ajustar Febrero
    if year < 1 or month < 1 or month > 12:
        return None
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_year_leap(year):
        return 29
    return month_days[month - 1]

def day_of_year(year, month, day):
    # Nivel 3: Depende de los niveles anteriores para el cálculo total
    
    # Verificamos si la combinación año/mes/día es físicamente posible
    max_days = days_in_month(year, month)
    if max_days is None or day < 1 or day > max_days:
        return None
    
    total_days = 0
    # Sumamos los días de los meses anteriores
    for m in range(1, month):
        total_days += days_in_month(year, m)
    
    # Añadimos los días del mes en curso
    total_days += day
    return total_days