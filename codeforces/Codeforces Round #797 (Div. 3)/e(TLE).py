import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

from bisect import bisect_left

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    tot = 0
    b = []
    
    for i in range(n):
        tot += a[i]//k
        if a[i] % k != 0:
            b.append(a[i] % k)
    
    b = sorted(b)
    nb = len(b)
    vis = [0] * nb
    for i, x in enumerate(b):
        if vis[i] == 1:
            continue

        left = bisect_left(b, k-x)
        
        while left < nb and vis[left] == 1:
            left += 1
        if left == nb or i == left:
            continue

        vis[i] = 1
        vis[left] = 1
        tot += 1

    printf(tot)
                

        
