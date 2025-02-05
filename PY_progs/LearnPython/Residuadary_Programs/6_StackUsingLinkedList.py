class stack:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


def isEmpty(ptr):
    if ptr == None:
        return True
    else:
        return False


def isFull(ptr):
    newnode = stack(60)
    if newnode == None:
        return True
    else:
        return False


def push(ptr, val):
    if isFull(ptr):
        print("Stack is Full Now")
        return ptr
    else:
        if ptr == None:
            newnode = stack(val)
            newnode.next = ptr
            return newnode
        qtr = ptr
        ftr = qtr.next
        while ftr != None:
            qtr = qtr.next
            ftr = ftr.next

        newnode = stack(val)
        newnode.next = None
        qtr.next = newnode
        return ptr


def pop(ptr):
    if isEmpty(ptr):
        print("Stack is Empty Now")
        return ptr
    else:
        if ptr == None:
            return None
        if ptr.next == None:
            ptr = ptr.next
            return ptr
        qtr = ptr
        ftr = qtr.next
        while ftr.next != None:
            qtr = qtr.next
            ftr = ftr.next
        qtr.next = ftr.next
        return ptr


def peek(ptr):
    arr = []
    while ptr != None:
        arr.append(ptr.data)
        ptr = ptr.next
    arr.reverse()
    print(*arr)


def stackBottom(ptr):
    if ptr == None:
        print("Stack is Empty Now")
        return ptr
    print("stack botton is", ptr.data)


def stackTop(ptr):
    if ptr == None:
        print("Stack is Empty Now")
        return ptr
    while ptr.next != None:
        ptr = ptr.next
    print("stack top is", ptr.data)


head = None

head = push(head, 10)
head = push(head, 20)
head = push(head, 30)
head = push(head, 40)
head = push(head, 50)
head = push(head, 60)
head = push(head, 70)
head = pop(head)
head = pop(head)


stackBottom(head)
stackTop(head)
