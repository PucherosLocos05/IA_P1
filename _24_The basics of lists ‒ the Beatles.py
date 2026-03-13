#Jesus Antonio Baez Ortega 23310372 6E
#LAB#24 The basics of lists ‒ the Beatles

# Step 1
beatles = []

# Step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Step 3
for member in ["Stu Sutcliffe", "Pete Best"]:
    name = input("añade miembro a la banda: ")
    beatles.append(name)

# Step 4
del beatles[3]
del beatles[3]

# Step 5
beatles.insert(0, "Ringo Starr")

print(beatles)