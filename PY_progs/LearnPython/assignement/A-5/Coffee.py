class Lion:
    x=10
    def __init__(self):
        print("hello i am Lion Contructor")
        def fun(self):
            print("Hello I am Fun Function")
class cub(Lion):
    y=20
    def __init__(self):
        super().__init__()
        super().fun()
        print("Hello I am Cub Constructor")
    def fun2(self):
        print("Hello I am Fun2 Function")
            
a=cub()
            