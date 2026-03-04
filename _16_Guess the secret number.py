#Jesus Antonio Baez Ortega 23310372 6E
#LAB#16 Guess the secret number

secretNumber = 111
condicion = False
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
while(condicion == False):
    choice = int(input("Ingresa el numero: "))
    if choice == secretNumber:
        condicion = True
    else: 
        print("Ha ha! You're stuck in my loop!")
print("Well done, muggle! You are free now.")