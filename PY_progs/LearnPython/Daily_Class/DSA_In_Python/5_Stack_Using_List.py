class Stack:
    arr = [None]
    size = None
    top = None

def isEmpty(ptr):
    if ptr.top == -1:
        return True
    else:
        return False

def isFull(ptr):
    if ptr.top == ptr.size-1:
        return True
    else:
        return False
    
def push(ptr, val):
    if isFull(ptr):
        print("Stack Full, Cant Push")
        return ptr
    else:
        ptr.top = ptr.top+1
        ptr.arr[ptr.top] = val
        return ptr

def Pop(ptr, val):
    
    

head = Stack()
head.size = 10
head.top = 1
head.arr= head.top*head.size
