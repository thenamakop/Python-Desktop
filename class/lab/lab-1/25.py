x: list = []
largest: int = 0
l = int(input("Enter the number of indices you want in the list"))
for i in range(l):
    L = int(input(f"Enter the value for the {i} index: "))
    x.append(L)
    print("Value Added successfully")
print("List has been made")
print(x)
