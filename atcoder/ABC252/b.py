from re import S
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

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

mx = max(a)
s = []
for i in range(n):
    if(a[i] == mx):
        s.append(i+1)

flag = False
for i in range(k):
    if(b[i] in s):
        flag = True
printf("Yes") if flag == True else printf("No")


