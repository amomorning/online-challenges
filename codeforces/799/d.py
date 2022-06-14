import sys
from webbrowser import get; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

def get_time(h, m):
    return h * 60 + m

def time_format(t):
    h = t // 60
    m = t % 60
    return "%02d:%02d"%(h, m)

def check(s):
    if s[0] == s[4] and s[1] == s[3]:
        return True
    return False

for _ in range(int(input())):
    s, x = input().split()
    x = int(x)
    h, m = map(int, s.split(':'))
    t = get_time(h, m)

    vis = [0] * 1440

    ans = 0
    for i in range(1440):
        cur = (t + i*x)%1440
        if vis[cur] == 1:
            break
        vis[cur] = 1

        if(check(time_format(cur))):
            # printf(time_format(cur))
            ans += 1
    printf(ans)
