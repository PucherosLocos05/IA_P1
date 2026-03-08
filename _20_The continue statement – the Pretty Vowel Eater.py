#Jesus Antonio Baez Ortega 23310372 6E
#LAB#20 The continue statement – the Ugly Vowel Eater

word = input("input a word: ")
word = word.upper()
word_without_vowels = ""

for i in word:
   if i != 'A' and i != 'E' and i != 'I' and i != 'O' and i != 'U' :
       word_without_vowels += i
print(word_without_vowels)
word_without_vowels = ""

for i in word: #forma mas "profesional"
    if i not in "AEIOU":
        word_without_vowels += i
print(word_without_vowels)
word_without_vowels = ""

for letter in word: #forma que pide el lab aunque sea muy idiota 

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
       word_without_vowels += letter
print(word_without_vowels)
word_without_vowels = ""