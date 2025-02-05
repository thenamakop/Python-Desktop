def fun(x):
    if x>=1:
        print(x)
        return fun(x-2)

print(fun(0))