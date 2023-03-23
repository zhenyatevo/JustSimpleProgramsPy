def swapMM(m):
    buf = min(m)
    buf1 = 0
    buf2 = 0
    for index in range(0, len(m)):
        if m[index] == min(m):
            buf1 = index
        elif m[index] == max(m):
            buf2 = index
    m[buf1] = max(m)
    m[buf2] = buf
    return m

ar1 = [4, 6, 2, 7,89, 1, 456, 55]
ar2 = [3, 10000, 345678, 34, 434, 2344, 56780, 9, 1, 342]

print(ar1)
print(swapMM(ar1))
print(ar2)
print(swapMM(ar2))
