x= [10,20,30,40,50]
x.append(0)

pos= int (input("Enter the position b/w 0to 5: "))
for i in range(len(x)-1,pos,-1):
    x[i]= x[i-1]
    
x[pos]= int (input("Enter your desired value: "))
print(x)    