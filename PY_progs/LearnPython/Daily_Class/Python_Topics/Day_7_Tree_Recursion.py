def fun(x,y):
    if x >=1:
        y=y+1
        fun(x-1,y)
        
        print(x,y)        
        fun(x-2,y)
        

fun(4,3)
