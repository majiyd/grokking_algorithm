def quickSort(arr):
    if len (arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lessThanPivot = [elem for elem in arr[1:] if elem < pivot]
        greaterThanPivot = [elem for elem in arr[1:] if elem >= pivot]
        return quickSort(lessThanPivot) + [pivot] + quickSort(greaterThanPivot)

print quickSort([10, 5, 2, 3, 4, 18, 12, 6, 9])