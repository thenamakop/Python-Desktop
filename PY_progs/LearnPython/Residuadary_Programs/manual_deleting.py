x=[34,55,10,22,19]
x.append(0)
pos=int(input("enter the position between 0 to 5"))
for i in range(pos,len(x)-1,1):
    x[i]=x[i+1]
print(x)