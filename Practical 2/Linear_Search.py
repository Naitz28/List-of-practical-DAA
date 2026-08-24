# =========================================================
# Linear Search - Standalone
#
# Time Complexity:
# Best Case    : O(1)
# Average Case : O(n)
# Worst Case   : O(n)
#
# Space Complexity:
# O(1)
# =========================================================

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def main():
    n = int(input("Enter number of elements: "))

    arr = list(map(int, input("Enter elements:\n").split()))

    key = int(input("Enter element to search: "))

    pos = linear_search(arr, key)

    if pos == -1:
        print("\nElement Not Found.")
    else:
        print(f"\nElement Found at Position {pos + 1}")


if __name__ == "__main__":
    main()