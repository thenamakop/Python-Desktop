def main():
    print("Welcome to the Roadmap Provider Project.")
    level = int(input("What is You level (Fresher/Experienced): "))
    RoadmapProvider(level)
def RoadmapProvider(level):
    if level == "1":
        print("Please enter your interest feild: ")
        interest = int(input("Enter 1 [WEB DEV], Enter 2 [APP DEV], or Enter 3 [DS, AI, ML] : "))
        if interest == 1:
            print("learn HTML, CSS, JavaScript, Pthon, BACKEND FRAMEWORK")
        elif interest == 2:
            print("Learn JAVA & DSA")
        elif interest == 3:
            print("Learn Python, Maths, R and 13+ skills")
        else:
            print("Please enter a valid option:")
            return
    elif level == "2":
        print("Please enter your interest feild: ")
        interest = int(input("Enter 1 [Data Analytics], Enter 2 [Cloud Computing], or Enter 3 [Front End] : "))
        if interest == 1:
            print("Learn Python, Excel, PowerB")
        elif interest == 2:
            print("Learn DevOps and Python for Automation")
        elif interest == 3:
            print("Learn Pythonand Django for Fromtend")
        else:
            print("Please enter a valid option:")
            
    else:
        print("Please enter a valid option:")
        return
    
if __name__ == "__main__":
    main()