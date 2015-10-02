def numDivisors(N):
    cnt = 0
    for i in range(1, N + 1):
        if N % i == 0:
            cnt += 1
    return cnt
print numDivisors(42)
