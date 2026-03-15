# Jesus Antonio Baez Ortega 23310372 6E
# LAB#18 the break statement – Stuck in a loop

x = True  # Variable centinela para mantener el bucle activo

while x == True:
    word = input("Insert a word: ")
    
    # Comparamos la entrada del usuario con la palabra secreta
    if word == "chupacabra":
        print("You have successfully left the loop.")
        break  # Termina el bucle inmediatamente y sale