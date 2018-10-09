def getSmallestElementIndex(arr):
    smallestElement = arr[0]
    smallestElementIndex = 0

    for i in range(len(arr)):
        if (arr[i] < smallestElement):
            smallestElement = arr[i]
            smallestElementIndex = i

    return smallestElementIndex

def selectionSort(arr):
    sortedArray = []
    for i in range(len(arr)):
        smallestElement = getSmallestElementIndex(arr)
        sortedArray.append(arr.pop(smallestElement))

    return sortedArray


myList = [42, 6, 8, 12, 32, 15, 12]
print(selectionSort(myList))