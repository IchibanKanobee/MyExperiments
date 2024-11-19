def find_sqrt(num):
    l, r = 0, num

    while True:
        mid = l + (r - l) // 2
        if mid * mid <= num < (mid + 1) * (mid + 1):
            return mid

        if (mid * mid) > num:
            r = mid
            continue

        if (mid * mid) < num:
            l = mid

print (find_sqrt(100))