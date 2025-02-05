def Binary_Search(arr, val):
    arr.sort()
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == val:
            return True
        elif arr[mid] < val:
            low = mid + 1
        elif arr[mid] > val:
            high = mid - 1
        else:
            print("No such value in array")
            return False


def Insert_Into_list(i):
    for j in range(i):
        ins = int(input("Please Insert a value into the array: "))
        arr.append(ins)
    print("All items added successfully!")
    print("Here is the final list: ", arr)


if __name__ == "__main__":
    arr: list = []
    i = int(input("Please specify the number of items you want to add to the array: "))
    Insert_Into_list(i)
    val = int(input("Please enter the number you want found in the array: "))
    old_index = arr.index(val)
    Binary_Search(arr, val)
    if Binary_Search(arr, val):
        print(f"Value {val} found at index (after sorting) ", arr.index(val))
        print(f"And it's original index was: {old_index}")
    elif Binary_Search(arr, val) is False:
        print(f"Value {val} not found in array/list")
    else:
        raise ValueError
