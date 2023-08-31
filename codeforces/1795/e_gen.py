#!/usr/bin/env python3
import random
T = 1
N = 5
MAX = 5

print(T)
print(N)
res = []
for i in range(N):
    res.append(random.randint(1, MAX))
print(' '.join(map(str, res)))

