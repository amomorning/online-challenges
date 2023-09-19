#!/usr/bin/env python3
import random
n = random.randint(1, 100)
m = random.randint(1, 100)
print(1)
print(n, m)
a = []
for i in range(n):
    a.append(str(random.randint(0, 100000)))
print(' '.join(a))
b = []
for i in range(m):
    b.append(str(random.randint(0, 100000)))
print(' '.join(b))

