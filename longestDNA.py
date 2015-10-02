import re
def longestDNA(s):
    res = ''
    lst = re.split(r'[^ACGT]', s)
    print lst
    for w in lst:
        if len(w) > len(res):
            res = w
    return res
print longestDNA('ACCGXXCXXGTTACTGGGCXTTGT')
    
