import itertools

def mex(a):
    a = sorted(a)
    for i in range(len(a)):
        if a[i] != i:
            return i
    return len(a)

def similar(a, b):
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            if mex(a[i:j]) != mex(b[i:j]):
                return False
    return True
    

n = 6
for p in itertools.permutations(range(n), n):
    tot = 0
    for p_ in itertools.permutations(range(n), n):
        if similar(p, p_):
            tot += 1
    if tot > 1: print(p, tot)
    
