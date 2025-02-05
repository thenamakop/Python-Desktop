def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
n = int(input("Enter a number: "))
print("The factorial of given no. i.e.",n,"is: ", factorial(n))
