import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printt(a):
    if LOCAL:
        printf(a)

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

n = int(input())
pre = list(map(int, input().split()))
ino = list(map(int, input().split()))


