def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def addPrimes(L):
    if len(L) == 0:
        return 0
    else:
        return addPrimes(L[1:]) + (L[0] if isPrime(L[0]) else 0)
