# Binary search algorithm

"""
Insertion sort algorithm

Binary Search: Used to find the insertion index efficiently, in O(log n) time.

Shifting Elements: For each insertion, elements to the right are shifted,
making the worst-case time complexity O(n^2) due to shifting, similar to insertion sort.
"""

def binary_insertion_sort(arr):
    def binary_search(arr, val, start, end):
        # Base case: if the range is empty
        if start == end:
            if arr[start] > val:
                return start
            else:
                return start + 1

        # If the range has two elements
        if start > end:
            return start

        # Middle element
        mid = (start + end) // 2
        if arr[mid] < val:
            return binary_search(arr, val, mid + 1, end)
        elif arr[mid] > val:
            return binary_search(arr, val, start, mid - 1)
        else:
            return mid

    for i in range(1, len(arr)):
        val = arr[i]
        # Find index where `val` should be inserted
        j = binary_search(arr, val, 0, i - 1)
        # Insert `val` at index `j` by shifting elements to the right
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
        print "inserted val: ", val + "\n"
    
    return arr

# Test the algorithm

arr = [5, 2, 8, 1, 9, 3, 6, 4, 7]
sorted_arr = binary_insertion_sort(arr)
print(sorted_arr)
