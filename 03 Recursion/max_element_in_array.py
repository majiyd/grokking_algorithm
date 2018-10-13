def getMaxElement(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] if arr[0] > getMaxElement(arr[1:]) else getMaxElement(arr[1:])




print(getMaxElement([23,4,6,7,12,56,18]))