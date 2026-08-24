def linear_search(arr, key):
    for i, value in enumerate(arr):
        if value == key:
            return i
    return -1


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

    if len(arr) != n:
        print(f"Please enter exactly {n} elements.")
        return

    key = int(input("Enter element to search: "))

    print("\nSearch Algorithms")
    print("1. Linear Search")
    print("2. Binary Search")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        position = linear_search(arr, key)

    elif choice == 2:
        if arr != sorted(arr):
            print("\nBinary search requires the array to be sorted.")
            return

        position = binary_search(arr, key)

    else:
        print("Invalid choice.")
        return

    if position == -1:
        print("\nElement not found.")
    else:
        print(f"\nElement found at position {position + 1}.")


if __name__ == "__main__":
    main()