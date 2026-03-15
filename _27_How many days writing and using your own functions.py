#Jesus Antonio Baez Ortega 23310372 6E
#LAB#27  How many days: writing and using your own functions

def is_year_leap(year):
    # Reusing the optimized logic from the previous step
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    # Validate arguments: Year must be positive, month must be 1-12
    if year < 1 or month < 1 or month > 12:
        return None
    
    # Days in each month (January is index 0, February index 1, etc.)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check for leap year February
    if month == 2 and is_year_leap(year):
        return 29
    
    return month_days[month - 1]

# --- Expanded Testing Code ---
test_years = [1900, 2000, 2016, 1987, 2024, 2023, 2023]
test_months = [2, 2, 1, 11, 2, 13, 6]
test_results = [28, 29, 31, 30, 29, None, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(f"{yr} {mo} -> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print(f"Failed (Expected {test_results[i]}, got {result})")