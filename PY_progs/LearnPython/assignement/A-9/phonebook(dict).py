x = {}

for i in range(3):
    key = input("Please Enter Name: ")
    pno = input("Please Enter the phone number: ")
    if len(pno) == 10:
        x[key] = pno
    else:
        print("Invalid Phone Number, Please enter a valid phone number")
    
print(x)