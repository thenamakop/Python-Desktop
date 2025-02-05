class Machine:
    x = 1550
    def __init__(self):
        print("Hello I am Machine constructor")
    def fun(self):
        print("Hello I am Machine function")
class Automobile(Machine):
    x = 1925
    def __init__(self):
        print("Hell I am automobile Constructor")
    def fun(self):
        print("Hello I am Automobile Function")
    
var = Automobile()
var.fun()
print("Year of Origin", var.x)