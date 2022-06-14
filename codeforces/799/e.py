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

    if sum(a) == s:
        printf(0)
        continue
    if sum(a) < s:
        printf(-1)
        continue

    interval = 0
    r = 0
    ans = 0
    for l in range(n):
        while interval < s and r < n:
            interval += a[r]
            r += 1

        while r < n and interval + a[r] == s:
            r += 1
        
        if interval == s:
            # printf([l, r, interval])
            ans = max(ans, r-l)

        interval -= a[l]
    printf(n-ans)
    
