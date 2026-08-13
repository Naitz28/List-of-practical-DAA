def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
arr = [18, 12, 2, 3, 1, 0]
print("before sorting:", arr)
selection_sort(arr)
print("after sorting:", arr)