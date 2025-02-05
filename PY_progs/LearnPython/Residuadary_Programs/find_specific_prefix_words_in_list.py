x = ["Lokesh","Karan","Karn","Rama","Ramayan","Karthik","Karina","Katrina"]

y=[]

for i in range(len(x)):
    if x[i].startswith("Ka"):
        y.append(x[i])
    
print(y)