import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)


from collections import deque
G = {}
def bfs(x, k):
    global G
    tot = []
    q = deque()
    q.append((x, 0))
    vis = {}

    while q:
        u, d = q.popleft()
        if u not in tot:
            tot.append(u)
        if d == k:
            continue

        for v in G[u]:
            if v not in vis:
                q.append((v, d+1))
            
    return sum(tot)

    


n, m = map(int, input().split())
for i in range(n):
    G[i+1] = []

for i in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)


for _ in range(int(input())):
    x, k = map(int, input().split())
    printf(bfs(x, k))


