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
    f = list(map(int, input().split()))
    s = input()

    F = {}

    for i in range(1, n+1):
        
        F[i] = [1, 0] if s[i-1] == 'W' else [0, 1]
    

    for i in range(n, 1, -1):
        fa = f[i-2]
        F[fa][0] += F[i][0]
        F[fa][1] += F[i][1]

        
    # printf(F)
        
    tot = 0
    for i in F:
        if(F[i][0] == F[i][1]):
            tot += 1
    printf(tot)
