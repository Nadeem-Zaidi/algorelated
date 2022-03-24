def sqrt(num, p):
    low = 0
    high = num
    ans = 1

    while low <= high:
        mid = (low + high) // 2
        if mid * mid == num:
            ans = mid
            break
        if mid * mid < num:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
            ans = mid

    i = 0.1
    for j in range(0, p):
        while ans * ans <= num:
            ans = ans + i
        ans = ans - i
        i = i / 10

    return ans


s=sqrt(7, 5)
print(s)
