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
    
    
def count_node(ptr):
    if ptr==None:
        return 0
    return 1+count_node(ptr.left)+count_node(ptr.right)
        
        
def count_height(ptr,h=0):
    if ptr==None:
        return h
    return max(count_height(ptr.left,h+1),count_height(ptr.right,h+1))
    
     
        

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


totalheight=count_height(a)
print(totalheight)