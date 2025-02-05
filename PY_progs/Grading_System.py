def Grading_System(Marks):
    if Marks >= 90:
        print(" Outstanding ")
        return
    elif Marks >= 80:
        print("Excellent")
        return
    elif Marks >= 70:
        print("Very Good")
        return
    elif Marks >= 60:
        print("Good")
        return
    elif Marks >=50:
        print("Pass")
        return   
    elif Marks < 50:
        print("Fail")
        return
    else:
        print("Invalid Input")


def main():
    print("Welcome to the Grading System")
    print("Enter your marks to calculate your grade")
    Marks = int(input("Enter your marks : "))
    Grading_System(Marks)
    
main()