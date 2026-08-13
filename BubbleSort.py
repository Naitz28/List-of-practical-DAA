def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = [18,12,2,3,1,0]
print("before sorting:",arr)
bubble_sort(arr)
print("after sorting:",arr)
