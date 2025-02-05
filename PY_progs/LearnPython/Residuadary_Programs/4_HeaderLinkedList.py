class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


def insertionATB(ptr, val):
    if ptr == None:
        head = Node(1)
        newnode = Node(val)
        head.next = newnode
        newnode.next = None
        return head
    newnode = Node(val)
    newnode.next = ptr.next
    ptr.next = newnode
    ptr.data = ptr.data + 1
    return ptr


def insertionATEND(ptr, val):
    if ptr == None:
        head = Node(1)
        newnode = Node(val)
        head.next = newnode
        newnode.next = None
        return head
    qtr = ptr
    ftr = qtr.next
    while ftr != None:
        qtr = qtr.next
        ftr = ftr.next
    newnode = Node(val)
    newnode.next = None
    qtr.next = newnode
    ptr.data = ptr.data + 1
    return ptr


def deletionATB(ptr):
    if ptr == None:
        return None
    qtr = ptr.next
    ptr.next = qtr.next
    ptr.data = ptr.data - 1
    return ptr


def deletionATEND(ptr):
    if ptr == None:
        return None
    qtr = ptr
    ftr = qtr.next
    while ftr.next != None:
        qtr = qtr.next
        ftr = ftr.next
    qtr.next = ftr.next
    ptr.data = ptr.data - 1
    return ptr


def Traversal(ptr):
    while ptr != None:
        print(ptr.data)
        ptr = ptr.next


head = Node(5)

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)

head.next = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = None

a = insertionATB(head, 60)
a = insertionATEND(head, 70)

a = deletionATB(head)
a = deletionATEND(head)
Traversal(head)
