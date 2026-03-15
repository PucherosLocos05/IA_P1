#Jesus Antonio Baez Ortega 23310372 6E
#LAB#28 Day of the year: writing and using your own functions
def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    if year < 1 or month < 1 or month > 12:
        return None
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_year_leap(year):
        return 29
    return month_days[month - 1]

def day_of_year(year, month, day):
    # 1. Validate the month and year using our previous function
    max_days = days_in_month(year, month)
    
    # 2. If month/year is invalid OR day is out of range (1 to max_days)
    if max_days is None or day < 1 or day > max_days:
        return None
    
    # 3. Sum the days of all months before the current one
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)
    
    # 4. Add the days of the current month
    total_days += day
    return total_days

# --- Testing Code ---
test_cases = [
    (2000, 12, 31, 366),  # Leap year end
    (2023, 12, 31, 365),  # Common year end
    (1900, 3, 1, 60),     # Non-leap year March 1st (Feb has 28)
    (2000, 3, 1, 61),     # Leap year March 1st (Feb has 29)
    (2024, 2, 29, 60),    # Leap day
    (2023, 2, 29, None),  # Invalid date (Feb 29 on common year)
    (2023, 13, 1, None)   # Invalid month
]

for yr, mo, dy, expected in test_cases:
    result = day_of_year(yr, mo, dy)
    print(f"{yr}-{mo:02d}-{dy:02d} -> {result}", end=" ")
    if result == expected:
        print("OK")
    else:
        print(f"FAILED (Expected {expected})")