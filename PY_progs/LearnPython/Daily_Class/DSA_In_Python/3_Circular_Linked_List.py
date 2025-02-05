class Node:
    data = None
    next = None
    def __init__(self, data):
        self.data = data


def Traversal(ptr):
    qtr = ptr
    print(qtr.data)
    qtr = qtr.next
    while qtr != ptr:
        print(qtr.data)
        qtr = qtr.next

def InsertionAtB(ptr, val):
    qtr = ptr
    while qtr.next != ptr:
        qtr = qtr.next
    newnode = Node(val)
    newnode.next = qtr.next
    qtr.next = newnode
    return newnode

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.next = b
b.next = c
c.next = d
d.next = a
