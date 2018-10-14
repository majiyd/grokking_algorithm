import random

def quickSort(arr):
    if len (arr) < 2:
        return arr
    else:
        pivot = arr[random.randint(0, len(arr) - 1)]
        arr.remove(pivot)
        lessThanPivot = [elem for elem in arr if elem < pivot]
        greaterThanPivot = [elem for elem in arr if elem >= pivot]
        return quickSort(lessThanPivot) + [pivot] + quickSort(greaterThanPivot)

print quickSort([10, 5, 3, 2, 3, 4, 18, 12, 6, 9,9,9])
