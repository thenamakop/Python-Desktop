class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


def Traversal(Ptr):
    while Ptr is not None:
        print(Ptr.data)
        Ptr = Ptr.next


def insertionATB(Ptr, val):
    newnode = Node(val)
    newnode.next = Ptr
    return newnode


def InsertionAtMiddle(Ptr, val, index):
    if Ptr is None:
        newnode = Node(val)
        newnode.next = Ptr
        return newnode
    copyptr = Ptr
    count = 0
    while copyptr is not None:
        count += 1
        copyptr = copyptr.next
    if count > index:
        qtr = Ptr
        i = 0
        while i < index - 1:
            qtr = qtr.next
            i = i + 1
        newnode = Node(val)
        newnode.next = qtr.next
        qtr.next = newnode
        return Ptr
    else:
        print("Index Out Of Range")
        return Ptr


def insertionATEND(Ptr, val):
    if Ptr is None:
        newnode = Node(val)
        newnode.next = Ptr
        return newnode
    qtr = Ptr
    ftr = qtr.next
    while ftr is not None:
        qtr = qtr.next
        ftr = ftr.next
    newnode = Node(val)
    newnode.next = None
    qtr.next = newnode
    return Ptr


def InsertionAtSValB(Ptr, val, sval):
    if Ptr is None:
        newnode = Node(val)
        newnode.next = Ptr
        return newnode
    if Ptr.data == sval:
        newnode = Node(val)
        return newnode
    flag = False
    copyptr = Ptr
    while copyptr is not None:
        if copyptr.data == sval:
            flag = True
            break
        copyptr = copyptr.next
    if flag:
        qtr = Ptr
        ftr = qtr.next
        while ftr.data != sval:
            qtr = qtr.next
            ftr = ftr.next
        newnode = Node(val)
        newnode.next = ftr
        qtr.next = newnode
        return Ptr


def InsertionAtSValA(Ptr, val, sval):
    if Ptr is None:
        newnode = Node(val)
        newnode.next = Ptr
        return newnode
    if Ptr.data == sval:
        newnode = Node(val)
        newnode.next = Ptr.next
        Ptr.next = newnode
        return Ptr
    flag = False
    copyptr = Ptr
    while copyptr is not None:
        if copyptr.data == sval:
            flag = True
            break
        copyptr = copyptr.next
    if flag:
        qtr = Ptr
        ftr = qtr.next
        while ftr.data != sval:
            qtr = qtr.next
            ftr = ftr.next
        newnode = Node(val)
        newnode.next = ftr.next
        ftr.next = newnode
        return Ptr
    else:
        print("Element Not Found")
        return Ptr


a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = None

a = insertionATB(a, 0)
a = InsertionAtMiddle(a, 25, 3)
a = InsertionAtSValB(a, 35, 40)
a = InsertionAtSValA(a, 45, 40)
a = insertionATEND(a, 60)
Traversal(a)
