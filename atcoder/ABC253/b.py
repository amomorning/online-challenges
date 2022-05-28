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

h, w = map(int, input().split())
pos = []
for i in range(h):
    s = input()
    for j, c in enumerate(s):
        if c == 'o':
            pos.append((i, j))

# import math

printf(abs(pos[0][0] - pos[1][0]) + abs(pos[0][1] - pos[1][1]))

