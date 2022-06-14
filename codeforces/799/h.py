import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

from math import inf

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    mp = {}
    for i in range(n):
        if a[i] in mp:
            mp[a[i]].append(i)
        else:
            mp[a[i]] = [i]
    
    ans = (-inf, -1, -1, -1)
    for k in mp:
        s = (inf, -1)
        m = len(mp[k])

        for i in range(m-1, -1, -1):
            p = mp[k][i]
            s = min(s, (m-i-(n-p-(m-i)), p))
            ans = max(ans, (m-i-(n-p-(m-i))-s[0], k, p, s[1]))

    print(ans[1], ans[2]+1, ans[3]+1)

    