#title display
print("Career Guidance Project")

level = input("Enter 1 [FRESHER], Enter 2 [EXPERIENCED] = ") #input string

if level == "1": #integer
    interest = input("Enter 1 [WEB DEV], Enter 2 [APP DEV], Enter 3 [DS,AI,ML] = ")
    if interest == "1":
        print("Learn HTML, CSS, JS, PYTHON, Backend Framework")
    
    elif interest == "2":
        print("Learn Java + DSA")
    
    elif interest == "3":
        print("Learn Python, Maths, 13+ Skills")

    else:
        print("In-valid input")

elif level == "2":
    interest = input("Enter 1 [DATA ANALYTICS], Enter 2 [CLOUD COOMP], Enter 3 [FRONT-END] = ")
    if interest == "1":
        print("Learn python, excel, PowerBI")

    elif interest == "2":
        print("Learn Devops, Python for scripting")

    elif interest == "3":
        print("Learn python & backend framework")

    else:
        print("In-valid input")

else:
    print("In-valid input")