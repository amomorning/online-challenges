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
    s = input().split('W')
    flag = True
    for x in s:
        if(len(x) == 0):
            continue
        if x.find('RB') == -1 and x.find('BR') == -1:
            flag = False
    
    printf("YES") if flag else printf("NO")
