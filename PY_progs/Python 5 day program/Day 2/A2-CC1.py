#Implement a Python script and create a variable and store the user's name through an i. Once the name is stored, the script should output a greeting that is personalised to the name given.
# For instance, if the input name is "Alice", the output should be "Hello, Alice!"


def greeting(name):
    print("Hello,", name+"!")

x = input("Please enter your name: ")
greeting(x)