# =========================================================
# Binary Search - Standalone
#
# Note:
# Array must be sorted in ascending order.
#
# Time Complexity:
# Best Case    : O(1)
# Average Case : O(log n)
# Worst Case   : O(log n)
#
# Space Complexity:
# O(1)
# =========================================================

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
     
    n = int(input("Enter number of elements: "))

    arr = list(map(int, input("Enter elements:\n").split()))

    key = int(input("Enter element to search: "))

    # Optional: ensure sorted for binary search
    arr.sort()

    pos = binary_search(arr, key)

    if pos == -1:
        print("\nElement Not Found.")
    else:
        print(f"\nElement Found at Position {pos + 1}")


if __name__ == "__main__":
    main()