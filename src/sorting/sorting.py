# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    #  Your code here
    # A helper function to merge two arrays.
    
    a = b = c = 0

    for c in range(len(merged_arr)):
        if b > len(arrB) - 1:
            merged_arr[c] = arrA[a]
            a += 1
        elif a > len(arrA) - 1:
            merged_arr[c] = arrB[b]
            b += 1

        elif arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            a +=1
        elif arrB[b] < arrA[a]:
            merged_arr[c] = arrB[b]
            b +=  1















    # while a < len(arrA) and b < len(arrB):
    #     if arrA[a] < arrB[b]:
    #         merged_arr[c] = arrA[a]
    #         c = c + 1
    #         a = a + 1

    #     else:
    #         merged_arr[c] = arrA[b]
    #         c = c + 1
    #         b = b + 1  
    # while a < len(arrA):
    #     merged_arr[c] = arrA[a]
    #     c = c + 1
    #     a = a + 1  

    # while b < len(arrB):
    #     c = c + 1
    #     b = b + 1




    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    arrA = arr[: len(arr) // 2]
    arrB = arr[len(arr) // 2:]        
    return merge(merge_sort(arrA), merge_sort(arrB))




    # return arr

#  STRETCH: implement the recursive logic for merge sort in a way that doesn't 
#  utilize any extra memory
#  In other words, your implementation should not allocate any additional lists 
#  or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here
