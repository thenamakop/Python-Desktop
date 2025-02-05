def fibbo(n):
    if n<=1:
        return n 
    else:
        return fibbo(n-1)+fibbo(n-2)

f = int(input("Please input a number eyou want fibbonacci series of: "))
for i in range(f):
    print(fibbo(i))