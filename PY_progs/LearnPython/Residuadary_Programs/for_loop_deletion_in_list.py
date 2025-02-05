x=[10,20,30,40,50,60,70,80]
print(x)
for i in range(len(x)):
    x.pop()
    print(x)
    if x == []:
        print("Stack has been emptied, all elements have been deleted")
print(x)