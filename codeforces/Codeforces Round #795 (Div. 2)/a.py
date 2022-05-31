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

    odd = 0
    even = 0
    for x in a:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    printf(min(even, odd))



