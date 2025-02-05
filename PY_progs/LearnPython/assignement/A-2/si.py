P = int(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = int(input("Enter the time frame (in years):  "))

SI = (P*R*T)/100

print("The simple interest on your principle amount i.e.", P, " with the rate", R, " and the time frame of", T," year(s) is Rs ", SI)
print("Then the final amount payable at the end of your time frame will be: Rs ",P+SI)