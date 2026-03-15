#Jesus Antonio Baez Ortega 23310372 6E
#LAB#26 A leap year: writing your own functions
def is_year_leap(year):
    # Check if divisible by 4
    if year % 4 == 0:
        # Check if it's a century year
        if year % 100 == 0:
            # Check if it's divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# --- Testing Code ---
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "-> ", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")