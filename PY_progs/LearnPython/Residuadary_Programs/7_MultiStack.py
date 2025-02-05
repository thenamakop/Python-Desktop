class stack:
    arr = [None]
    size = None
    top1 = None
    top2 = None


def isEmpty(ptr):
    if ptr.top1 == -1 and ptr.top2 == ptr.size:
        return True
    else:
        return False


def isFull(ptr):
    if ptr.top1 + 1 == ptr.top2:
        return True
    else:
        return False


def push1(ptr, val):
    if isFull(ptr):
        print("Stack is Full Now Guys")
        return ptr
    else:
        ptr.top1 = ptr.top1 + 1
        ptr.arr[ptr.top1] = val
        return ptr


def push2(ptr, val):
    if isFull(ptr):
        print("Stack is Full Now")
        return ptr
    else:
        ptr.top2 = ptr.top2 - 1
        ptr.arr[ptr.top2] = val
        return ptr


def pop1(ptr):
    if isEmpty(ptr):
        print("Stack is Empty Now")
        return ptr
    else:
        ptr.arr[ptr.top1] = None
        ptr.top1 = ptr.top1 - 1
        return ptr


def pop2(ptr):
    if isEmpty(ptr):
        print("Stack is Empty Now")
        return ptr
    else:
        ptr.arr[ptr.top2] = None
        ptr.top2 = ptr.top2 + 1
        return ptr


def peek1(ptr):
    for i in range(ptr.top1, -1, -1):
        print(ptr.arr[i])


def peek2(ptr):
    for i in range(ptr.size - 1, ptr.top2 - 1, -1):
        print(ptr.arr[i])


head = stack()
head.size = 10
head.arr = head.arr * head.size
head.top1 = -1
head.top2 = head.size


head = push1(head, 10)
head = push1(head, 20)
head = push1(head, 30)
head = push1(head, 40)
head = push2(head, 50)
head = push2(head, 60)
head = push2(head, 70)
head = push2(head, 80)
head = push2(head, 90)
head = push2(head, 100)


peek1(head)
peek2(head)
