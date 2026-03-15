# Jesus Antonio Baez Ortega 23310372 6E
# LAB#20 The continue statement – the Pretty Vowel Eater

word = input("Ingresa una palabra: ")
word = word.upper()
word_without_vowels = "" # Variable acumuladora

for letter in word:
    if letter == "A":
        continue # Salta a la siguiente iteración
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        # Si no es vocal, se "concatena" a nuestra variable
        word_without_vowels += letter

print("Palabra sin vocales:", word_without_vowels)