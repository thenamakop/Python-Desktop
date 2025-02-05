x = [11,22,33,44,55]

y = [66,77,88,99,110]

z = [0,1,2,3,4,5,6,]
print(x)
print(y)
print(z)
for i in range(len(y)-1):
    x.append(y[i])
    
print(x)
x.extend(z)
print(x)

    