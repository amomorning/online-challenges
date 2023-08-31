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
    s = input()
    
    if(len(s) == 2):
        printf(s[1])
        continue

    mn = 0x3f3f3f3f
    for c in s:
        x = int(c)
        mn = min(mn, x)
    printf(mn)
