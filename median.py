def median(L):
    L.sort()
    n = len(L)
    m = n / 2
    return (L[m - 1] + L[m]) / 2 if n % 2 == 0 else L[m]
print median( [ 1.0, 100.0, 2.0 ] )
print median([ 1.0, 100.0, 2.0, 3.0 ])
