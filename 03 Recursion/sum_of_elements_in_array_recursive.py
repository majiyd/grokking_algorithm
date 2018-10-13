#This is how i figured it on my own
# def sum_of_array(arr, ans):
#     while arr:
#         ans+=arr.pop(0)
#     return ans
#
# print(sum_of_array([1, 2, 3, 4], 0))

#my solution after studying grokking algoorithm

def sum_of_array(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum_of_array(arr[1:])

print(sum_of_array([1, 2, 3, 4]))