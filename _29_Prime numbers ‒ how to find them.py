# Jesus Antonio Baez Ortega 23310372 6E
# LAB#29 Prime numbers ‒ how to find them

def is_prime(num):
    # Paso 1: Por definición, los números menores a 2 no son primos
    if num < 2:
        return False
    
    # Paso 2: Optimización matemática. 
    # Buscamos divisores solo hasta la raíz cuadrada del número.
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            # Si el residuo es 0, encontramos un divisor: no es primo
            return False 
            
    # Paso 3: Si el bucle termina sin encontrar divisores, es primo
    return True 

# --- Código de Prueba ---
# Probamos los números del 2 al 20
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()