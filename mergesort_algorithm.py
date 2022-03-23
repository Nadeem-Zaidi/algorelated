def MergeSort(arr):
    if len(arr) < 2:
        return
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:]
    MergeSort(left)
    MergeSort(right)
    merge(arr, left, right)


def merge(a, l, r):
    i = 0
    j = 0
    k = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        a[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        a[k] = r[j]
        j += 1
        k += 1


t = [34, 67, 1, 90, 3, 9, 13, 17, -90, 67, 10, 0]

MergeSort(t)
print(t)
tt=[67,0,9.5]
MergeSort(tt)
print(tt)
