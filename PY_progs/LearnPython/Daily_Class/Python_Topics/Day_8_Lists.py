x = [54,65,23,10,18,92]

first = 0
last = len(x) - 1

while first < last:
    x[first], x[last] = x[last], x[first]
    first += 1
    last -= 1

print(x)


for i in range(0,len(x)//2,1):
    temp=x[i]
    x[i], x[len(x)-1-i]=x[len(x)-1-i], temp
    
print(x)