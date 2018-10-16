def mergeSort(arr):
    sizeOfArray = len(arr)
    if sizeOfArray > 1:
        mid = sizeOfArray/2
        leftSide = arr[:mid]
        rightSide = arr[mid:]
        mergeSort(leftSide)
        mergeSort(rightSide)
        leftSide.append(float('inf'))
        rightSide.append(float('inf'))
        leftCounter = 0
        rightCounter = 0
        for i in range(len(arr)):
            if leftSide[leftCounter]  <= rightSide[rightCounter]:
                arr[i] = leftSide[leftCounter]
                leftCounter+=1
            else:
                arr[i] = rightSide[rightCounter]
                rightCounter += 1


    return arr

print mergeSort([10, 5, 2, 3, 4, 18, 12, 6, 9])