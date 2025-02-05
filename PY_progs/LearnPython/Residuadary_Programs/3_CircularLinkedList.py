class Node:
    data=None
    next=None
    def __init__(self,data):
        self.data=data
 
def insertionATB(ptr,val):
    if ptr==None:
        newnode=Node(val)
        newnode.next=None
        return newnode
    if ptr.next==None:
        newnode=Node(val)
        newnode.next=ptr
        ptr.next=newnode
        return ptr
    qtr=ptr
    while qtr.next!=ptr:
        qtr=qtr.next
    newnode=Node(val)
    newnode.next=qtr.next
    qtr.next=newnode
    return newnode



def insertionATEND(ptr,val):
    if ptr==None:
        newnode=Node(val)
        newnode.next=None
        return newnode
    if ptr.next==None:
        newnode=Node(val)
        newnode.next=ptr
        ptr.next=newnode
        return ptr
    qtr=ptr
    while qtr.next!=ptr:
        qtr=qtr.next
    newnode=Node(val)
    newnode.next=qtr.next
    qtr.next=newnode
    return ptr


def deletionATB(ptr):
    if ptr==None:
        return None
    if ptr.next==None:
        return None
    qtr=ptr
    ftr=qtr.next
    while ftr!=ptr:
        ftr=ftr.next
        qtr=qtr.next
    qtr.next=ftr.next
    return ftr.next



def Traversal(ptr):
    qtr=ptr
    print(qtr.data)
    qtr=qtr.next
    while qtr!=ptr:
        print(qtr.data)
        qtr=qtr.next
  
def deletionATEND(ptr):
    if ptr==None:
        return None
    if ptr.next==None:
        return None
    qtr=ptr
    ftr=qtr.next
    while ftr.next!=ptr:
        ftr=ftr.next
        qtr=qtr.next
    qtr.next=ftr.next
    return ftr.next

a=Node(10)
b=Node(20)
c=Node(30)
d=Node(40)


a.next=b
b.next=c
c.next=d
d.next=a

a=insertionATB(a,50)
a=insertionATEND(a,60)
a=deletionATB(a)
a=deletionATEND(a)
Traversal(a)