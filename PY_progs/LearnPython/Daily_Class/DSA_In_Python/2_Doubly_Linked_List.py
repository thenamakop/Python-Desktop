class Node:
    data = None
    next = None
    prev = None

    def __init__(self, data):
        self.data = data


def insertionATB(ptr, val):
    newnode = Node(val)
    newnode.next = ptr
    newnode.prev = None
    ptr.prev = newnode
    return newnode


def insertionATEND(ptr, val):
    if ptr is None:
        return insertionATB(ptr, val)
    qtr = ptr
    ftr = qtr.next
    while ftr is not None:
        qtr = qtr.next
        ftr = ftr.next

    newnode = Node(val)
    newnode.next = None
    newnode.prev = qtr
    qtr.next = newnode
    return ptr


def insertionATBT(ptr, val, index):
    if ptr is None:
        return insertionATB(ptr, val)
    if index == 0:
        return insertionATB(ptr, val)
    count = 0
    copyptr = ptr
    while copyptr is not None:
        count = count + 1
        copyptr = copyptr.next
    if count > index:
        qtr = ptr
        ftr = qtr.next
        i = 0
        while i < index - 1:
            qtr = qtr.next
            ftr = ftr.next
            i = i + 1

        newnode = Node(val)
        newnode.next = ftr
        newnode.prev = qtr
        qtr.next = newnode
        ftr.prev = newnode
        return ptr
    else:
        print("index out of range")
        return ptr


def insertATSVB(ptr, val, sval):
    if ptr is None:
        return insertionATB(ptr, val)
    if ptr.data == sval:
        return insertionATB(ptr, val)
    flag = False
    copyptr = ptr
    while copyptr is not None:
        if copyptr.data == sval:
            flag = True
            break
        copyptr = copyptr.next

    if flag:
        qtr = ptr
        ftr = qtr.next
        while ftr.data != sval:
            qtr = qtr.next
            ftr = ftr.next
        newnode = Node(val)
        newnode.next = ftr
        newnode.prev = qtr
        qtr.next = newnode
        ftr.prev = newnode
        return ptr
    else:
        print("element not found")
        return ptr


def insertionATSVA(ptr, val, sval):
    if ptr is None:
        return insertionATB(ptr, val)
    if ptr.data == sval:
        newnode = Node(val)
        newnode.next = ptr.next
        newnode.prev = ptr
        ptr.next.prev = newnode
        ptr.next = newnode
        return ptr
    flag = False
    copyptr = ptr
    while copyptr is not None:
        if copyptr.data == sval:
            flag = True
            break
        copyptr = copyptr.next
    if flag is True:
        qtr = ptr
        while qtr.data != sval:
            qtr = qtr.next
        if qtr.next is None:
            return insertionATEND(ptr, val)
        newnode = Node(val)
        newnode.next = qtr.next
        newnode.prev = qtr
        qtr.next.prev = newnode
        qtr.next = newnode
        return ptr
    else:
        print("element not found")
        return ptr


def deletionATB(ptr):
    if ptr is None:
        return None
    ptr = ptr.next
    ptr.prev = None
    return ptr


def deletionATEND(ptr):
    if ptr is None:
        return None
    if ptr.next is None:
        return deletionATB(ptr)
    qtr = ptr
    ftr = qtr.next
    while ftr.next is not None:
        ftr = ftr.next
        qtr = qtr.next
    qtr.next = None
    ftr.prev = None
    return ptr


def deletionATBT(ptr, index):
    if ptr is None:
        return None
    if index == 0:
        return deletionATB(ptr)
    count = 0
    copyptr = ptr
    while copyptr is not None:
        count = count + 1
        copyptr = copyptr.next
    if count > index:
        qtr = ptr
        ftr = qtr.next
        i = 0
        while i < index - 1:
            qtr = qtr.next
            ftr = ftr.next
            i = i + 1
        if ftr.next is None:
            return deletionATEND(ptr)
        qtr.next = ftr.next
        ftr.next.prev = qtr
        ftr.prev = None
        ftr.next = None
        return ptr
    else:
        print("index out of range")
        return ptr


def deletionATSV(ptr, sval):
    if ptr is None:
        return None
    if ptr.data == sval:
        return deletionATB(ptr)
    flag = False
    copyptr = ptr
    while copyptr is not None:
        if copyptr.data == sval:
            flag = True
            break
        copyptr = copyptr.next

    if flag:
        qtr = ptr
        ftr = qtr.next
        while ftr.data != sval:
            ftr = ftr.next
            qtr = qtr.next
        if ftr.next is None:
            return deletionATEND(ptr)
        qtr.next = ftr.next
        ftr.next.prev = qtr
        return ptr
    else:
        print("Node not found")
        return ptr


def Traversal(ptr):
    while ptr is not None:
        print(ptr.data)
        ptr = ptr.next


def TraversalRev(ptr):
    if ptr is None:
        return None
    qtr = ptr.next
    while qtr is not None:
        ptr = ptr.next
        qtr = qtr.next
    while ptr is not None:
        print(ptr.data)
        ptr = ptr.prev


# def Sorting(ptr):
#     arr=[]
#     while ptr is not None:
#         arr.append(ptr.data)
#         ptr=ptr.next
#     arr.sort()
#     for i in range(len(arr)):
#         ptr=insertionATEND(ptr,arr[i])
#     return ptr

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.prev = None
a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = d
d.prev = c
d.next = None


a = insertionATB(a, 50)
a = insertionATEND(a, 60)
a = insertionATBT(a, 80, 3)
a = insertionATBT(a, 90, 0)
a = insertATSVB(a, 100, 60)
a = insertATSVB(a, 110, 90)
a = insertionATSVA(a, 100, 60)
a = deletionATB(a)
a = deletionATB(a)
a = deletionATEND(a)
a = deletionATSV(a, 60)
a = deletionATSV(a, 80)
# a = Sorting(a)
Traversal(a)
