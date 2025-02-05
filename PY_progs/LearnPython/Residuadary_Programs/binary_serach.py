def binary_search(arr, val):
    arr.sort()
    print("The sorted array is: ", arr)
    low = 0
    high = (len(arr)-1)
    while low <= high :
        mid = low + (high -low)// 2
        if arr[mid] == val:
            return True
        elif arr[mid] < val:
            low = mid + 1
        elif arr[mid] > val:
            high = mid - 1
        else:
            return False
def Insert_Into_List():
    items = int(input("How Many Items You want to add in the list: "))
    for i in range(items):
        ins=int(input("Please Insert a value into the list: "))
        arr.append(ins)
arr=[]    
Insert_Into_List()
print(arr)
val = int(input("Please enter the value you want found: "))
binary_search(arr, val)
if binary_search(arr, val):
    print(f"value {val} found at index (after sorting) ", arr.index(val))
else :
    print(f"value {val} not found in array/list")