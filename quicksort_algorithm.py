def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if len(arr) == 1:
        return
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)


t = [12, 56, 90, 23, 56, 9, 3, 13, 17, -900, 0, 4]
size = len(t)
# p=partition(t, 0, size - 1)
# print(p)
# print(t)
quicksort(t, 0, size - 1)
print(t)
