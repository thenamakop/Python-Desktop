def linear_search(arr, t):
    for i in range(len(arr)):
        if arr[i] == t:
            return i
    return -1


if __name__ == "__main__":
    arr = [3, 5, 2, 9, 1, 7, 4]
    try:
        t = int(input("Enter target integer: "))
    except ValueError:
        print("Invalid input")
        raise SystemExit(1)

    idx = linear_search(arr, t)
    if idx != -1:
        print(f"Found at index {idx}")
    else:
        print("Not Found")