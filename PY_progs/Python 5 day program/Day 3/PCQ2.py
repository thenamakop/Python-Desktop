#Grading System(10M)
#Task: Develop a program that calculates the final grade of a student based on
#their marks. The grading system is as follows:
#● Below 50: Fail
#● 50 to 59: Pass
#● 60 to 69: Good
#● 70 to 79: Very Good
#● 80 to 89: Excellent
#● 90 and above: Outstanding
#Input Format: The program should prompt the user to enter the student's
#marks as a single integer.

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