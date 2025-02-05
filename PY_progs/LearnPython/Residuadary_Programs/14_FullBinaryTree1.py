class Tree:
    left=None
    right=None
    data=None
    def __init__(self,data):
        self.data=data
  

def preOrder(ptr):
    if ptr==None:
        return None
    print(ptr.data)
    preOrder(ptr.left)
    preOrder(ptr.right)
    
def inOrder(ptr):
    if ptr==None:
        return None
    inOrder(ptr.left)
    print(ptr.data)
    inOrder(ptr.right)

def postOrder(ptr):
    if ptr==None:
        return None
    postOrder(ptr.left)
    postOrder(ptr.right)
    print(ptr.data)
    
def isFullBinaryTree(ptr):
    if ptr==None:
        return True
    elif ptr.left==None and ptr.right==None:
        return True
    elif ptr.left!=None and ptr.right!=None:
        return isFullBinaryTree(ptr.left) and isFullBinaryTree(ptr.right)
    elif ptr.left==None and ptr.right!=None:
        return False
    elif ptr.left!=None and ptr.right==None:
        return False
    
    

a=Tree(10)
b=Tree(20)
c=Tree(30)
d=Tree(40)
e=Tree(50)
f=Tree(60)
g=Tree(70)


a.left=b
a.right=c

b.left=d
b.right=e

c.left=f
c.right=g


flag=isFullBinaryTree(a)
if flag==True:
    print("Full Binary Tree")
else:
    print("Not Full Binary Tree")