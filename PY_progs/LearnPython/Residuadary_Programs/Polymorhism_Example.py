class Mummy:
    x=10
    def __init__(self):
        print("Hello I am Mummy Constructor")
    def fun(self):
            print("Hello I am Mummy Function")
            
class Papa(Mummy):
    x=66
    def __init__(self):
        print("Hello I am Papa Constructor")
    def fun(self):
        print("Hello I am Papa Function")
        
a = Papa()
a.fun()
print(a.x)
        