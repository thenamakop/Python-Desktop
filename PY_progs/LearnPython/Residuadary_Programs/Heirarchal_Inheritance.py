class flower:
    def __init__(self):
        print("hello i am Flower Contructor")

    def std(self):
        print("Hello I am parent Function")

class r_rose(flower):
    def __init__(self):
        #super().__init__()
        #super().std()
        print("Hello I am rose Constructor")
    
    def r_std(self):
        print("Hello I am red one Function")
        
class w_rose(flower):
    def __init__(self):
        #super().__init__()
        #super().std()
        print("Hello I am rose Constructor")
    
    def w_std(self):
        print("Hello I am white one Function")

        
a=r_rose()
a.r_std()

b=w_rose()
b.w_std()