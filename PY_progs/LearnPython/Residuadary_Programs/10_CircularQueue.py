class queue:
    arr = [None]
    front = None
    rear = None
    size = None


def isEmpty(ptr):
    if ptr.front == ptr.rear:
        return True
    else:
        return False


def isFull(ptr):
    if (ptr.rear + 1) % ptr.size == ptr.front:
        return True
    else:
        return False


def enqueue(ptr, val):
    if isFull(ptr):
        print("Queue is Full Now")
        return ptr
    else:
        ptr.rear = (ptr.rear + 1) % ptr.size
        ptr.arr[ptr.rear] = val
        return ptr


def dequeue(ptr):
    if isEmpty(ptr):
        print("Queue is Empty Now")
        return ptr
    else:
        ptr.front = (ptr.front + 1) % ptr.size
        ptr.arr[ptr.front] = None
        return ptr


def display(ptr):
    ptr.front = (ptr.front + 1) % (ptr.size)
    while ptr.front != ptr.rear + 1:
        print(ptr.arr[ptr.front])
        ptr.front = (ptr.front + 1) % (ptr.size)


head = queue()
head.size = 10
head.front = -1
head.rear = -1
head.arr = head.arr * head.size

head = enqueue(head, 10)
head = enqueue(head, 20)
head = enqueue(head, 30)
head = enqueue(head, 40)
head = enqueue(head, 50)
head = enqueue(head, 60)
head = enqueue(head, 70)
head = enqueue(head, 80)
head = enqueue(head, 90)
head = enqueue(head, 100)
head = enqueue(head, 110)

head = dequeue(head)

head = enqueue(head, 150)
head = enqueue(head, 160)
head = dequeue(head)
head = dequeue(head)

head = enqueue(head, 10)
head = enqueue(head, 20)
head = enqueue(head, 30)
head = enqueue(head, 40)
head = enqueue(head, 50)

head = dequeue(head)
head = dequeue(head)
head = dequeue(head)
head = dequeue(head)
head = dequeue(head)
display(head)
