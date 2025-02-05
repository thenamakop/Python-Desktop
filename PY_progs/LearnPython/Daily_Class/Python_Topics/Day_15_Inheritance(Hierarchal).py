from typing import Any


class Father:
    surname = "Gupta"
    def __init__(self):
        print("Hello I am Father constructor")
    def fun(self):
        print("Hello I am Father function")
    def last_name(self):
        print(self.surname)

class Son1(Father):
    def __init__(self):
        super().__init__()
        print("I am Son1 constructor")
    def fun(self):
        print("Hello I am Son1 function")
        super().fun()
        super().last_name()

class Son2(Father):
    def __init__(self):
        super().__init__()
        print("I am Son2 constructor")
        
    def fun(self):
        print("Hello I am Son2 function")
        super().fun()
        super().last_name()
        
a = Son1()
b = Son2()
a() 
b()
