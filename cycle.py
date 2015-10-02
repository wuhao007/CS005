def cycle(S, n):
    m = len(S)
    return (S[:m-n][::-1] + S[m-n:][::-1])[::-1] 
print cycle('1110110000', 2)
