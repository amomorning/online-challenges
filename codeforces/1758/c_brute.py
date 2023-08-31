a = [4, 2, 3, 5, 1]
from itertools import permutations

def check(arr):
    for i, a in enumerate(arr):
        if arr[i] % (i+1) != 0:
            return False
    return True

for x in permutations(a):
    if check(x):
        print(x)

