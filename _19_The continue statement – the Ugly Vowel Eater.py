# Jesus Antonio Baez Ortega 23310372 6E
# LAB#19 The continue statement – the Ugly Vowel Eater

word = input("Ingresa una palabra: ")
word = word.upper() # Convertimos a mayúsculas para comparar fácilmente

for letter in word:
    # Si la letra es una vocal, el 'continue' hace que el bucle
    # ignore el print de abajo y pase a la siguiente letra.
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        # Solo llegamos aquí si NO se ejecutó ningún 'continue'
        print(letter)