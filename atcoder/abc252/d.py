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

N = int(2e5 + 1)
n = int(input())
a = list(map(int, input().split()))

ca = [0] * N
for x in a:
    ca[x] += 1

z = []
for x in ca:
    if x != 0:
        z.append(x)

tot = 0
suffix = [0]
prefix = [0]
lz = len(z)
for i in range(lz):
    suffix.append(z[i] + suffix[i])
    prefix.append(z[lz-i-1]+ prefix[i])
for i in range(lz):
    tot += z[i] * suffix[i] * prefix[lz-i-1]

printf(tot)


