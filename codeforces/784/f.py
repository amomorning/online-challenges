import sys;input=lambda:sys.stdin.readline().strip("\r\n")
import platform
LOCAL = (platform.uname().node == 'AMO')
# print(LOCAL)
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

    prefix = [a[0]]
    suffix = [a[n-1]]
    for i in range(1, n):
        
        prefix.append(a[i] + prefix[i-1])
        suffix.append(a[n-i-1] + suffix[i-1])
    
    suffix.reverse()

    l, r = 0, n-1

    res = 0
    while(l < r):
        while(suffix[r] < prefix[l] and l + 1 < r):
            r -= 1
        if(suffix[r] == prefix[l]):
            res = n-r+l+1
        l += 1
    
    printf(res)
