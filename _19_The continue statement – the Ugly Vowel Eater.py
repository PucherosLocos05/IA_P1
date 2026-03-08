#Jesus Antonio Baez Ortega 23310372 6E
#LAB#19 The continue statement – the Ugly Vowel Eater

word = input("input a word: ")
word = word.upper()

for i in word:
   if i != 'A' and i != 'E' and i != 'I' and i != 'O' and i != 'U' :
      print(i)


for i in word: #forma mas "profesional"
    if i not in "AEIOU":
        print(i)
    

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
       
        print(letter)