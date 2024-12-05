# Sorting and Searching Application in Python
# This app provides various sorting and searching algorithms
# with detailed comments for clarity and understanding.

# Sorting Algorithms

def selection_sort(arr):
    """Selection Sort: Sorts an array by repeatedly finding the minimum element and placing it at the beginning."""
    for i in range(len(arr)):
        # Find the minimum element in unsorted part
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def bubble_sort(arr):
    """Bubble Sort: Repeatedly steps through the list, compares adjacent items, and swaps them if they are in the wrong order."""
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    """Insertion Sort: Builds the sorted array one item at a time by inserting elements in the correct order."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """Merge Sort: Divides the array into halves, sorts each half, and merges them back together."""
    if len(arr) > 1:
        # Find the middle point and divide the array
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr):
    """Quick Sort: Picks a pivot element and partitions the array around it."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Taking the first element as pivot
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


# Searching Algorithms

def linear_search(arr, target):
    """Linear Search: Iterates through the array to find the target element."""
    for index, element in enumerate(arr):
        if element == target:
            return index  # Target found
    return -1  # Target not found


def binary_search(arr, target):
    """Binary Search: Efficiently finds target element in a sorted array by dividing the search range in half."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        # Check if the target is at the mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore the right half
        else:
            right = mid - 1
    return -1  # Target not found


# Application Menu

def main():
    """Main function to run the Sorting and Searching application."""
    print("Welcome to the Sorting and Searching Application")
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print("\nChoose a Sorting Algorithm:")
    print("1. Selection Sort")
    print("2. Bubble Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    choice = int(input("Enter your choice (1-5): "))

    sorted_arr = []
    if choice == 1:
        sorted_arr = selection_sort(arr.copy())
    elif choice == 2:
        sorted_arr = bubble_sort(arr.copy())
    elif choice == 3:
        sorted_arr = insertion_sort(arr.copy())
    elif choice == 4:
        sorted_arr = merge_sort(arr.copy())
    elif choice == 5:
        sorted_arr = quick_sort(arr.copy())
    else:
        print("Invalid choice!")
        return

    print("Sorted Array:", sorted_arr)

    print("\nChoose a Searching Algorithm:")
    print("1. Linear Search")
    print("2. Binary Search (Requires sorted array)")
    search_choice = int(input("Enter your choice (1-2): "))
    target = int(input("Enter the number to search for: "))

    result = -1
    if search_choice == 1:
        result = linear_search(arr, target)
    elif search_choice == 2:
        result = binary_search(sorted_arr, target)  # Binary search on sorted array
    else:
        print("Invalid choice!")
        return

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")


# Run the application
if __name__ == "__main__":
    main()
