#Jesus Antonio Baez Ortega 23310372 6E
#LAB#25 Operating with lists ‒ basics

numbers = [1, 2, 3, 2, 4, 3, 5, 1, 6]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print("Lista original: ", numbers)
print("Lista sin repeticiones:", unique)