import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

def calc_step(x):
    tmp = x
    cnt = 0
    while tmp % 2 == 0:
        tmp /= 2
        cnt += 1
    return cnt

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    even = 0
    mn_step = 0x3f3f3f3f
    for i in range(n):
        if a[i] % 2 == 0:
            even += 1
            mn_step = min(calc_step(a[i]), mn_step)
    
    if even != n:
        printf(even)
    else:
        printf(mn_step + even - 1)


