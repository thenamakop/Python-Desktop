class Tree:
    left=None
    right=None
    data=None
    def __init__(self,data):
        self.data=data

BST=[]


def inOrder(ptr):
    if ptr==None:
        return None
    inOrder(ptr.left)
    print(ptr.data)
    inOrder(ptr.right)
    
def insertDataInBst(ptr):
    if ptr==None:
        return None
    insertDataInBst(ptr.left)
    BST.append(ptr.data)
    insertDataInBst(ptr.right)
 
def isBST(arr):
    flag=False
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            flag=True
        else:
            flag=False
            break
    if flag==True:
        print("This Tree is BST")
    else:
        print("This Tree is not BST")
            
       
def SearchingInBST(ptr,sval):
    if ptr==None:
        return False
    elif ptr.data==sval:
        return True
    elif ptr.data>sval:
        return SearchingInBST(ptr.left,sval)
    elif ptr.data<sval:
        return SearchingInBST(ptr.right,sval)
   
 
def insertionInBST(ptr,val):
    if ptr==None:
        newnode=Tree(val)
        return newnode
    elif ptr.data>val:
        ptr.left=insertionInBST(ptr.left,val)
    elif ptr.data<val:
        ptr.right=insertionInBST(ptr.right,val)
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
    return ptr
    
    
  
 
a=Tree(2)
b=Tree(5)
c=Tree(1)
d=Tree(15)
e=Tree(21)
f=Tree(60)
g=Tree(7)
h=Tree(45)

a.left=c
a.right=b
b.right=d
d.left=g
d.right=e
e.right=f
f.left=h


a=deletionInBST(a,2)
inOrder(a)