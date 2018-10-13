def countElement(arr):
    if arr == []:
        return 0
    else:
        return 1 + countElement(arr[1:])

print(countElement([1, 2, 3, 4]))