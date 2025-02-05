x = []

for i in range(4):
    x.append([])
    for j in range(4):
        temp = int(input("Enter the value of the matrix : "))
        x[i].append(temp)
    
print(x)