class Queue:
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
    if ptr.rear == ptr.size - 1:
        return True
    else:
        return False


def enqueue(ptr, val):
    if isFull(ptr):
        print("QueueFull")
        return ptr
    else:
        ptr.rear = ptr.rear + 1
        ptr.arr[ptr.rear] = val
        return ptr


def dequeue(ptr, val):
    if isEmpty(ptr):
        print("Queue Empty")
        return ptr
    else:
        ptr.front = ptr.front + 1
        ptr.arr[ptr.front] = None
        return ptr


def Display(ptr):
    for i in range(ptr.front + 1, ptr.rear + 1, 1):
        print(ptr.arr[i])


head = Queue()
head.size = 10
head.arr = head.arr * head.size


head.front = -1
head.rear = -1



Display(head)