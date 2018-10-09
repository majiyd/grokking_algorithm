def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while  (low <= high):
        mid = (low + high)/2

        if (arr[mid] == item):
            return mid


        elif (arr[mid] < item):
            low = mid + 1

        else:
            high = mid - 1
    return None

myList = [1,3,5,7,9,11]

print(binary_search(myList, -1))
