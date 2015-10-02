def indexNearest42(L):
    res = 0
    m = abs(L[0] - 42)
    for i in range(1, len(L)):
        n = L[i]
        if abs(n - 42) < m:
            m = abs(n - 42)
            res = i
    return res
