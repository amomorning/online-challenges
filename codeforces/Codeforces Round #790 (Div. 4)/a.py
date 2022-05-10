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
    first = int(s[0]) + int(s[1]) + int(s[2])
    last = int(s[3]) + int(s[4]) + int(s[5])
    
    printf("YES") if first == last else printf("NO")
