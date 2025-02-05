count=0
num=int(input("Enter the value of the num "))
i=1
while i<=num:
    if num%i==0:
        count=count+1
        i=i+1
    if count==2:
            print("It is prime number")
    else:
        print("it is not a prime number")