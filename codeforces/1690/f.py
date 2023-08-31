import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

        

from math import gcd
for _ in range(int(input())):
    n = int(input())
    s = input()
    a = list(map(lambda x: int(x)-1, input().split()))

    ans = 1
    vis = [0] * n
    for i in range(n):
        if vis[i] == 0:

            cur = i
            cycle = s[i]
            while a[cur] != i:
                vis[cur] = 1
                cur = a[cur]

                cycle += s[cur]
            period = (cycle + cycle).find(cycle, 1)
            ans = ans // gcd(ans, period) * period
    printf(ans)
        
        
