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
    n = int(input())
    a = list(map(int, input().split()))

    mp = {}
    for i in range(n):
        if a[i] in mp:
            mp[a[i]] += 1
        else:
            mp[a[i]] = 1

    cnt = 0
    for i in mp.keys():
        if mp[i] % 2 == 0:
            cnt += 1
    ans = len(mp)
    if cnt % 2 != 0:
        ans -= 1
    printf(ans)
