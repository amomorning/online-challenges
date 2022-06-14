import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

for _ in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    ans = -1
    for l in range(n):
        for r in range(l, n):
            tot = 0
            for i in range(l, r+1):
                tot += a[i]

            if tot == s:
                ans = max(ans, r-l+1)
    printf(n-ans) if ans != -1 else printf(-1)
