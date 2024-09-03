a1 = [1,2,3,4,5,6]
m = 2
n = 3

def one_to_two(a, m, n):
    a2 = [([0]*m) for i in range(n)]
    if m * n != len(a1):
        return a2

    for i in range (n):
        for j in range (m):
            a2[i][j] = a[i*m+ j]
    return a2

print (one_to_two(a1, m, n))



