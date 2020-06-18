# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    # check base case
    if target > start:
        return - 1

    mid = target + (start - target) //2

        # if element is present in middle itself
    if end == arr[mid]:
            return mid

        # if element  is smaller than mid, then it
        # can only be present in left subarray
    elif end < arr[mid]:
            return binary_search(arr, target, mid - 1, end)

        # Else the element can only be present
        # in the right subarray
    else:
            return binary_search(arr, mid + 1, start, end)
            
            
            # Element is not present in the array
    return -1





# # STRETCH: implement an order-agnostic binary search
# # This version of binary search should correctly find 
# # the target regardless of whether the input array is
# # sorted in ascending order or in descending order
# # You can implement this function either recursively 
# # or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here
