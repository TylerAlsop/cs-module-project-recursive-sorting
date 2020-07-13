# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    arrA_index = 0
    arrB_index = 0
    merged_arr_index = 0

    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] < arrB[arrB_index]:
            merged_arr[merged_arr_index] = arrA[arrA_index]
            merged_arr_index += 1
            arrA_index += 1
        else:
            merged_arr[merged_arr_index] = arrB[arrB_index]
            merged_arr_index += 1
            arrB_index += 1

    while arrA_index < len(arrA):
        merged_arr[merged_arr_index] = arrA[arrA_index]
        merged_arr_index += 1
        arrA_index += 1
    while arrB_index < len(arrB):
        merged_arr[merged_arr_index] = arrB[arrB_index]
        merged_arr_index += 1
        arrB_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    middle_index = int(len(arr) // 2)
    left_arr = arr[:middle_index]
    right_arr = arr[middle_index:]

    if len(arr) > 1:
        left_half = merge_sort(left_arr)
        right_half = merge_sort(right_arr)
        arr = merge(left_half, right_half)


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

