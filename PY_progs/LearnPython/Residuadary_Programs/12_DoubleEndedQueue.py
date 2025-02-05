class queue:
    arr=[]
    size=None

def isEmpty(ptr):
    if len(ptr.arr)==0:
        return True
    else:
        return False

def isFull(ptr):
    if len(ptr.arr)==ptr.size:
        return True
    else:
        return False
  
def enqueueB(ptr,val):
    if isFull(ptr):
        print("Queue is Full Now")
        return ptr
    else:
        ptr.arr.insert(0,val)
        return ptr

def enqueueE(ptr,val):
    if isFull(ptr):
        print("Queue is Full Now")
        return ptr  
    else:
               
        ptr.arr.append(val)
        return ptr
  
def dequeueB(ptr):
    if isEmpty(ptr):
        print("Queue is Empty Now")
        return ptr
    else:
        del ptr.arr[0]
        return ptr

def dequeueE(ptr):
    if isEmpty(ptr):
        print("Queue is Empty Now")
        return ptr
    else:
        ptr.arr.pop()
        return ptr
   
def display(ptr):
    for i in range(len(ptr.arr)):
        print(ptr.arr[i]) 
        
        
head=queue()
head.size=10

head=enqueueB(head,10)
head=enqueueB(head,20)
head=enqueueB(head,30)
head=enqueueB(head,40)
head=enqueueE(head,50)
head=enqueueE(head,60)
head=enqueueE(head,70)
head=enqueueE(head,80)
head=enqueueB(head,90)
head=enqueueB(head,100)

head=dequeueB(head)
head=dequeueB(head)
head=dequeueB(head)
head=dequeueB(head)
head=dequeueB(head)
head=dequeueB(head)
head=dequeueB(head)

head=dequeueE(head)
head=dequeueE(head)
head=dequeueE(head)
head=dequeueE(head)
head=dequeueE(head)
head=dequeueE(head)
display(head)


    
    