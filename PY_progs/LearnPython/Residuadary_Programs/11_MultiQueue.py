class queue:
    arr = [None]
    frontB = None
    rearB = None
    frontE = None
    rearE = None
    size = None


def isEmpty(ptr):
    if ptr.frontB == ptr.rearB and ptr.frontE == ptr.rearE:
        return True
    else:
        return False


def isFull(ptr):
    if ptr.rearB + 1 == ptr.rearE:
        return True
    else:
        return False


def enqueueB(ptr, data):
    if isFull(ptr):
        print("Queue is Full Now")
        return ptr
    else:
        ptr.rearB = ptr.rearB + 1
        ptr.arr[ptr.rearB] = data
        return ptr


def enqueueE(ptr, data):
    if isFull(ptr):
        print("Queue is Full Now")
        return ptr
    else:
        ptr.rearE = ptr.rearE - 1
        ptr.arr[ptr.rearE] = data
        return ptr


def dequeueB(ptr):
    if isEmpty(ptr):
        print("Queue is Empty Now")
        return ptr
    else:
        ptr.frontB = ptr.frontB + 1
        ptr.arr[ptr.frontB] = None
        return ptr


def dequeueE(ptr):
    if isEmpty(ptr):
        print("Queue is Empty Now")
        return ptr
    else:
        ptr.frontE = ptr.frontE - 1
        ptr.arr[ptr.frontE] = None
        return ptr


def display(ptr):
    for i in range(ptr.frontB + 1, ptr.rearB + 1, 1):
        print(ptr.arr[i])
    for i in range(ptr.frontE - 1, ptr.rearE - 1, -1):
        print(ptr.arr[i])


head = queue()
head.size = 10
head.arr = head.arr * head.size
head.frontB = -1
head.rearB = -1
head.frontE = head.size
head.rearE = head.size

head = enqueueB(head, 10)
head = enqueueB(head, 20)
head = enqueueB(head, 30)
head = enqueueB(head, 40)
head = enqueueE(head, 50)
head = enqueueE(head, 60)
head = enqueueE(head, 70)
head = enqueueE(head, 80)
head = enqueueB(head, 90)
head = enqueueB(head, 100)


display(head)
