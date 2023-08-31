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
    s = input()

    id = len(s)//2
    tot = 0
    for i in range(id, n):
        if(s[i] == s[id]):
            tot += 1
        else:
            break
    for i in range(id-1, -1, -1):
        if(s[i] == s[id]):
            tot += 1
        else:
            break
    printf(tot)


