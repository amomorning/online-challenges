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
    n, k = map(int, input().split())
    s = input()

    ans = 0
    for i in range(k):
        ans += int(s[i] == 'W')
    
    tot, r = ans, k
    for l in range(n-k):
        tot -= int(s[l] == 'W')
        while r - l <= k:
            tot += int(s[r] == 'W')
            r += 1
        ans = min(ans, tot)
    printf(ans)
