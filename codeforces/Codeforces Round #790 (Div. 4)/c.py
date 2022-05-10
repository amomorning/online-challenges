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

def diff(a, b, m):
    tot = 0
    for i in range(m):
        
        tot += abs(ord(a[i]) - ord(b[i])) 
    return tot


for _ in range(int(input())):
    n, m = map(int, input().split())

    s = []
    for i in range(n):
        s.append(input())
    
    mn = 0x3f3f3f3f
    for i in range(n):
        for j in range(i):
            
            mn = min(mn, diff(s[i], s[j], m))
    
    printf(mn)
