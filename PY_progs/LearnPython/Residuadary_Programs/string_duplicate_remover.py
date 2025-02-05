x = "Maulik is a good student"
y = ""

for i in range(len(x)):
    if x[i] not in y:
        y += x[i]

print(y)
