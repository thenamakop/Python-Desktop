class flower:
    def __init__(self):
        print("hello i am Flower Contructor")

    def std(self):
        print("Hello I am parent Function")

class rose:
    def __init__(self):
        #super().__init__()
        #super().std()
        print("Hello I am rose Constructor")
    
    def std1(self):
        print("Hello I am std one Function")

class red_rose(flower,rose):
    def __init__(self):
        supper().__init__()
        print("I am construtor of red rose ")
    def red_rose(self):
        print("Hello I am a red_rose function")
        
x=red_rose()