#!/usr/bin/env python3
import random
print(1)
n, m = 7, 6
print(n, m)
for i in range(n):
    print(random.randint(1, m), end=' ')
print('')

cold = []
for i in range(m):
    cold.append(random.randint(1, 10))
    print(cold[i], end=' ')
print('')

for i in range(m):
    print(random.randint(1, cold[i]), end=' ')
print('')
