def symmetric(S):
    n = len(S)
    for i in range(n):
        for j in range(i, n):
            if S[i][j] != S[j][i]:
                return False
    return True
