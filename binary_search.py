# ----------------------------------------------------------------------------
# ***************************** BINARY SEARCH ********************************
# ----------------------------------------------------------------------------

# Binary Search is a searching algorithm that finds the position of a target value within a sorted array.Binary Search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found.

# Time Complexity: O(log n) where n is the number of elements in the list
# Space Complexity: O(1)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

    
# Example
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = binary_search(arr, x)

    if result == -1:
        print(f'The value {x} is not present in the list')
    else:
        print(f'The value {x} found at index {result+1}')