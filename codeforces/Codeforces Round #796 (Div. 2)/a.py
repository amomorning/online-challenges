import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

for _ in range(int(input())):
    x = int(input())

    if x == 1:
        printf(3)
        continue

    s = list(str(bin(x)))
    s.reverse()
    cnt = 0
    for c in s:
        if c == '1':
            break
        cnt += 1
        
    if x == 1 << cnt:
        printf(x + 1)
    else:
        printf(1 << cnt)
