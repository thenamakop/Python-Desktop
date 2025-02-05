
try:
    x = int(input("Please enter a integer value"))


    if x==0:
        print("The Entered numer is zero.")
    elif x<0:
        print("The Entered numer is is negative.")
    else:
        print("The Entered numer is positive.")
except ValueError:
    print("the entered value is invalid.")  