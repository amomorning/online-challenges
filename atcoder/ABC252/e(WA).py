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

n, m = map(int, input().split())

edges = []
for i in range(m):
    u, v, c = map(int, input().split())
    edges.append({'u': u-1, 'v': v-1, 'c': c, 'id': i})

edges = sorted(edges, key=lambda k:k['c'])

fa = []
sz = [1] * n
for i in range(n):
    fa.append(i)

def find(x):
    if x != fa[x]: 
        fa[x] = find(fa[x])
    return fa[x]

def union(x, y):
    xx = find(x); yy = find(y)
    if xx == yy:
        return
    if sz[xx] > sz[yy]: 
        xx, yy = yy, xx
    fa[xx] = yy
    sz[yy] = sz[yy] + sz[xx]


result = []
for e in edges:
    fu = find(e['u'])
    fv = find(e['v'])
    if(fu != fv):
        result.append(e['id']+1)
        union(fu, fv)

printf(result)
