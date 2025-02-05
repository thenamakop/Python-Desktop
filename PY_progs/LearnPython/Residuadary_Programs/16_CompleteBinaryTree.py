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
   
   
def isCompleteBinaryTree(ptr,index,totalnode):
    if ptr==None:
        return True
    elif index>=totalnode:
        return False
    return isCompleteBinaryTree(ptr.left,2*index+1,totalnode) and isCompleteBinaryTree(ptr.right,2*index+2,totalnode) 
    
def count_node(ptr):
    if ptr==None:
        return 0
    return 1+count_node(ptr.left)+count_node(ptr.right)



a=Tree(10)
b=Tree(20)
c=Tree(30)
d=Tree(40)
e=Tree(50)
f=Tree(60)
g=Tree(70)


a.left=b
a.right=c

# b.left=d
# b.right=e

c.left=f
c.right=g


totalnode=count_node(a)

if isCompleteBinaryTree(a,0,totalnode)==True:
    print("Complete Binary Tree")
else:
    print("Not Complete Binary Tree")