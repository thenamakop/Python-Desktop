class stack:
    arr = [None]
    size = None
    top = None


def isEmpty(ptr):
    if ptr.top == -1:
        return True
    else:
        return False


def isFull(ptr):
    if ptr.top == ptr.size - 1:
        return True
    else:
        return False


def push(ptr, val):
    if isFull(ptr):
        print("Stack is Full Now")
        return ptr
    else:
        ptr.top = ptr.top + 1
        ptr.arr[ptr.top] = val
        return ptr


def pop(ptr):
    if isEmpty(ptr):
        print("Stack is Empty Now")
        return ptr
    else:
        ptr.arr[ptr.top] = None
        ptr.top = ptr.top - 1
        return ptr


def stackTop(ptr):
    if ptr.top == -1:
        print("Stack is Empty Now")
        return ptr
    print(ptr.arr[ptr.top])


def stackBottom(ptr):
    if ptr.top == -1:
        print("Stack is Empty Now")
        return ptr
    print(ptr.arr[0])


def peek(ptr):
    for i in range(ptr.top, -1, -1):
        print(ptr.arr[i])


head = stack()
head.size = 10
head.top = -1
head.arr = head.arr * head.size

head = push(head, 5)
head = push(head, 10)
head = push(head, 15)
head = push(head, 20)
head = push(head, 25)
head = push(head, 30)
head = push(head, 35)
head = push(head, 40)
head = push(head, 45)
head = push(head, 50)

head = pop(head)
head = pop(head)
head = pop(head)
head = pop(head)
head = pop(head)
head = pop(head)
head = pop(head)
head = pop(head)

peek(head)
