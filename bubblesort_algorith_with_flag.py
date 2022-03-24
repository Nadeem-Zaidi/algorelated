def BubbleSort(arr):
    if len(arr) < 2:
        return
    for i in range(len(arr)):
        isSwaped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                isSwaped = True
        if not isSwaped:
            break


t = [56, 0, 7, 13, 29, 17, -5]
BubbleSort(t)
print(t)

tt = [90]
BubbleSort(tt)
print(tt)
