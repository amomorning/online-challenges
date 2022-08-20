from functools import cmp_to_key

def cmp(a, b):
    if len(a) == len(b): 
        if a > b: return 1
        elif a < b: return -1
        else: return 0
    if len(a) > len(b): return 1
    elif len(a) < len(b): return -1
    else: return 0

n = int(input())
a = sorted(input().split(), key=cmp_to_key(cmp), reverse=True)[:3]
# print(a)
print(''.join(sorted(a, reverse=True)))


