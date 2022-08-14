import itertools

import math

def lcm(a, b):
    # print(a, b)
    # print(math.gcd(a, b))
    # print(a*b//math.gcd(a, b))
    return a*b//math.gcd(a, b)


n = 9
ans = (0, [])
for p in itertools.permutations(range(1, n+1), n):
    tot = 0
    for i in range(1, n+1):
        tot += lcm(i, p[i-1])
    if tot > ans[0]:
        ans = (tot, [p])
    elif tot == ans[0]:
        ans[1].append(p)
print(ans)
