class Tree:
    left=None
    right=None
    data=None
    height=1
    def __init__(self,data):
        self.data=data

def getheight(ptr):
    if ptr==None:
        return 0
    return ptr.height


def getBalanceFactor(ptr):
    if ptr==None:
        return 0
    return getheight(ptr.left)-getheight(ptr.right)
       

def rightRotation(y):
    x=y.left
    t2=x.right
    x.right=y
    y.left=t2
    
    y.height=max(getheight(y.left),getheight(y.right))+1
    x.height=max(getheight(x.left),getheight(x.right))+1
    return x
    
def leftRotation(x):
    y=x.right
    t2=y.left
    y.left=x
    x.right=t2
    
    y.height=max(getheight(y.left),getheight(y.right))+1
    x.height=max(getheight(x.left),getheight(x.right))+1
    return y

def inOrder(ptr):
    if ptr==None:
        return None
    inOrder(ptr.left)
    print(ptr.data)
    inOrder(ptr.right)
    

def insertionInAVL(ptr,val):
    if ptr==None:
        newnode=Tree(val)
        return newnode
    elif ptr.data>val:
        ptr.left=insertionInAVL(ptr.left,val)
    elif ptr.data<val:
        ptr.right=insertionInAVL(ptr.right,val)
    
    ptr.height=1+max(getheight(ptr.left),getheight(ptr.right))    
    balance=getBalanceFactor(ptr)
    
    if balance>1:
        if getBalanceFactor(ptr.left)>=0:
            return rightRotation(ptr)
        else:
            ptr.left=leftRotation(ptr.left)
            return rightRotation(ptr)
    
    if balance<-1:
        if getBalanceFactor(ptr.right)<=0:
            return leftRotation(ptr)
        else:
            ptr.right=rightRotation(ptr.right)
            return leftRotation(ptr)
    
    return ptr


def findSuccessor(ptr):
    while ptr.left!=None:
        ptr=ptr.left
    return ptr



def deletionInBST(ptr,sval):
    if ptr==None:
        return None
    elif ptr.data>sval:
        ptr.left=deletionInBST(ptr.left,sval)
    elif ptr.data<sval:
        ptr.right=deletionInBST(ptr.right,sval)
    else:
        if ptr.left==None:
            temp=ptr.right
            ptr=None
            return temp
        if ptr.right==None:
            temp=ptr.left
            ptr=None
            return temp
        
        temp=findSuccessor(ptr.right)
        ptr.data=temp.data
        ptr.right=deletionInBST(ptr.right,temp.data)
        
    ptr.height=1+max(getheight(ptr.left),getheight(ptr.right))    
    balance=getBalanceFactor(ptr)
    
    if balance>1:
        if getBalanceFactor(ptr.left)>=0:
            return rightRotation(ptr)
        else:
            ptr.left=leftRotation(ptr.left)
            return rightRotation(ptr)
    
    if balance<-1:
        if getBalanceFactor(ptr.right)<=0:
            return leftRotation(ptr)
        else:
            ptr.right=rightRotation(ptr.right)
            return leftRotation(ptr)
    return ptr


a=None
a=insertionInAVL(a,33)
a=insertionInAVL(a,13)
a=insertionInAVL(a,53)
a=insertionInAVL(a,11)
a=insertionInAVL(a,21)
a=insertionInAVL(a,61)
a=insertionInAVL(a,8)
a=insertionInAVL(a,9)

inOrder(a)