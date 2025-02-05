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
    
def count_height(ptr,h=0):
    if ptr==None:
        return h
    return max(count_height(ptr.left,h+1),count_height(ptr.right,h+1))
def isPerfectBinaryTree(ptr,height,level=0):
    if ptr==None:
        return True
    elif ptr.left==None and ptr.right==None:
        return height==(level+1)
    elif ptr.left!=None and ptr.right==None:
        return None
    elif ptr.left==None and ptr.right!=None:
        return False
    elif ptr.left!=None and ptr.right!=None:
        return isPerfectBinaryTree(ptr.left,height,level+1) and isPerfectBinaryTree(ptr.right,height,level+1)
    
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


countheight=count_height(a)

if isPerfectBinaryTree(a,countheight)==True:
    print("Perfect Binary Tree")
else:
    print("Not Perfect Binary Tree")