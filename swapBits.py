def swapBits(S):
    return ''.join(map(lambda x: '1' if x == '0' else '0', S))
print swapBits('101011')
