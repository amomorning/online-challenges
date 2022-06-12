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
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    tot = sum(a)
    
    for i in range(n):
        a[i] -= n - i - 1

    # printf(tot)
    # printf(a)

    
    a = sorted(a)
    a.reverse()

    for i in range(k):
        tot -= a[i]
    tot -= k * (k-1) // 2
    printf(tot)
