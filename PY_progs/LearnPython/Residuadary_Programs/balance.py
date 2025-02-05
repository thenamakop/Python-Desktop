print("---Enter a value between  1 and 3---")
x = int(input("Please enter your choice: "))

balance = 1000

if x == 1:
    balance += 500
elif x == 2:
    balance -= 500
elif x == 3:
    balance *= 2
elif x == 4:
    print(balance)
else:
    print("Wrong Input")

