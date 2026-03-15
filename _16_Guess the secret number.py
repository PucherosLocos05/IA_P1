# Jesus Antonio Baez Ortega 23310372 6E
# LAB#16 Guess the secret number

secretNumber = 111
condicion = False  # Esta es nuestra "bandera" para controlar el bucle

print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)

# El bucle se repetirá infinitamente mientras 'condicion' sea False
while(condicion == False):
    choice = int(input("Ingresa el numero: "))
    
    if choice == secretNumber:
        condicion = True  # Al cambiar a True, el bucle terminará en la siguiente evaluación
    else: 
        # Si no adivina, el bucle vuelve a empezar
        print("Ha ha! You're stuck in my loop!")

# Este mensaje solo se ve cuando logramos salir del bucle
print("Well done, muggle! You are free now.")