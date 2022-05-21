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

n = int(input())
all_s = []
for i in range(n):
    all_s.append(input())


def solve(num):
    idx = []

    for i in range(n):
        s = all_s[i]
        idx.append(s.find(str(num)))

    idx = sorted(idx)
    res = []

    for x in idx:
        while x in res:
            x += 10
        res.append(x)
        
    # print('i =', num, end=': ')
    # printf(res)
    return max(res)

ans = 0x3f3f3f3f
for i in range(10):
    ans = min(ans, solve(i))

printf(ans)
