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

G = {}
F = {}

def dfs(u):
    global s

    w = 0
    b = 0
    for v in G[u]:
        dfs(v)
        w += F[v][0]
        b += F[v][1]
    
    if(s[u-1] == 'W'):
        w += 1
    else:
        b += 1
    
    F[u] = (w, b)




for _ in range(int(input())):
    n = int(input())
    f = list(map(int, input().split()))
    G = {}
    F = {}

    for i in range(1, n+1):
        G[i] = []
        F[i] = ()
    
    for i in range(n-1):
        G[f[i]].append(i+2)
    
    s = input()

    dfs(1)

    tot = 0
    for i in F:
        if(F[i][0] == F[i][1]):
            tot += 1
    printf(tot)
