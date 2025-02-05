class ram:
    _x=99
    __y=100
    __z=105
    def __init__(self):
        print(self._x)
        print("hello")
    def fun(self):
        print("Hello I am Fun Function")
class Raju(ram):
    def __init__(self):
        print(super()._x)
        print("hello i am Raju Constructor")

a=Raju()
print(a._ram__y)