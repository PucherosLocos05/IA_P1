#Jesus Antonio Baez Ortega 23310372 6E
#LAB#21 Essentials of the while loop

blocks = int(input())

height = 0
layer = 1

while blocks >= layer:
    blocks -= layer
    height += 1
    layer += 1

print("La altura de la piramide es:", height)