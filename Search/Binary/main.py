# Binary search algorithm

"""
Input: A sorted array and a target value.
Output: The index of the target in the array if found, else -1.
"""
import random

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        print(f"Current search range: arr[{left}:{right+1}]")
        print(f"Midpoint: {mid}, Value at midpoint: {arr[mid]}")
        if arr[mid] == target:
            print(f"Target {target} found at index {mid}")
            return mid
        elif arr[mid] < target:
            print(f"Target {target} is greater than {arr[mid]}, searching right half")
            left = mid + 1
        else:
            print(f"Target {target} is less than {arr[mid]}, searching left half")
            right = mid - 1

    print(f"Target {target} not found in the array")
    return -1


if __name__ == '__main__':
    # test algorithm
    arr = list(range(0, 1000000))  # Create a list of numbers from 0 to 999999
    target = random.randint(0, 999999)

    result = binary_search(arr, target)
    print(f"Result: {result}")
    