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

insertDataInBst(a)

isBST(BST)
