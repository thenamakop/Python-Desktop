import sampl

def SI():
    p = int(input("Principle amount: "))
    r = int(input("rate of interest: "))  
    t = int(input("time frame: "))
    x = (sampl.fun(p,r,t))
    print(f"the simple intrest on the principle value{p} at time{t} and rate of interest{r} is : {x}")
    print(f"The total payable amount at the end of the time frame{t} will be : {p+x}")