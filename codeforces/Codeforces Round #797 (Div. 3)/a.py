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
    n = int(input())
    
    for i in range(n//3, n//2+3):
        flag = False
        for j in range(1, 4):
            l = i - j
            r = n - i - l
            if r < l and r > 0:
                printf([l, i, r])
                flag = True
                break
        if flag:
            break
     
    

