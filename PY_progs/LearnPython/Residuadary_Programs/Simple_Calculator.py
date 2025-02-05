def calculator(x, y):
    try:
        print("Enter 1 to perform addition")
        print("enter 2 to perform subtaction")
        print("Enter 3 to perform multiplication")
        print("Enter 4 to perform division")
        print("Enter 0 to exit")
        i = int(input("Please Enter your choice of operation: "))
        if i == 1:
            print(
                f"The result of the additon of x and y i.e. {x} & {y}, respectively is:  {x+y}"
            )
        elif i == 2:
            print(
                f"The result of the subtraction of x and y i.e. {x} & {y}, respectively is:  {x-y}"
            )
        elif i == 3:
            print(
                f"The result of the multiplication of x and y i.e. {x} & {y}, respectively is:  {x*y}"
            )
        elif i == 4:
            print(
                f"The result of the division of x and y i.e. {x} & {y}, respectively is:  {x/y}"
            )
        elif i == 0:
            print("Thank You for using this Simple Calculator V1.0")
            exit()
        else:
            print("Please enter a valid choice")
            calculator(x, y)
        print("Do You want to use this program to perfom another operation ?")
        re_use()
    except:
        ZeroDivisionError
        print(
            "You are trying to divide by zero, please enter a non-zero integer for division."
        )


def re_use():
    re_user = int(input("If So, Please enter 1 else enter 0 to exit: "))
    if re_user == 1:
        x = int(input("Please Enter the first operand: "))
        y = int(input("Please Enter the second operand: "))
        calculator(x, y)
    elif re_user == 0:
        print("Thanks For using this program.")
        exit()
    else:
        print("Please choose a correct choice")


if __name__ == "__main__":
    x = int(input("Please Enter the first operand: "))
    y = int(input("Please Enter the second operand: "))
    calculator(x, y)
