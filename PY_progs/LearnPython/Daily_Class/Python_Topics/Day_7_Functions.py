
x = 88
fa = False
y = "Maulik"
def f():
    global x
    x = 66
    global fa
    fa = True
    global y
    y = "Gupta Ji" 
    print(x)
    print(not fa)
    print(y)
print(type(x),x)
print(type(fa),fa)
print(type(y),y)

    

f()
print(type(x),x)
print(type(fa),fa)
print(type(y),y)