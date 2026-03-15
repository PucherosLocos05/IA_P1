#Jesus Antonio Baez Ortega 23310372 6E
#LAB#29 Prime numbers ‒ how to find them
def is_prime(num):
    # Primes must be greater than 1
    if num < 2:
        return False
    
    # Check for divisors from 2 up to the square root of num
    # We use int(num**0.5) + 1 to ensure the range includes the square root
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Found a divisor, so it's not prime
            
    return True  # No divisors found, it's prime!

# --- Testing Code ---
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()