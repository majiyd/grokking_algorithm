def recursive_binary_search(arr, item, low, high):

    if (len(arr) == 1):
        if arr[0] == item:
            return 0

        else:
            return None

    elif len(arr) > 1:
        if low <= high:
            mid = (low + high)/2
            if (arr[mid] == item):
                return mid

            elif(arr[mid] < item):
                low = mid + 1
                recursive_binary_search(arr, item, low, high)
            else:
                high = mid - 1
                recursive_binary_search(arr, item, low, high)
        else:
            return None

    else:
        return None



myList = [1, 2, 3, 5, 9, 11, 13]
print(recursive_binary_search(myList, 9, 0, len(myList)-1))