import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

from math import sqrt
from collections import namedtuple
Point = namedtuple('Point',['x', 'y'])

n, k = map(int, input().split())
a = list(map(lambda x: int(x)-1, input().split()))

def distance(a, b):
    return sqrt((a.x - b.x)*(a.x - b.x) + (a.y - b.y)*(a.y - b.y))

pts = []
for i in range(n):
    x, y = map(int, input().split())
    pts.append(Point(x, y))

res = 0
for i in range(n):
    dist = 0x3f3f3f3f
    for _ in range(k):
        j = a[_]
        dist = min(dist, distance(pts[i], pts[j]))

    res = max(res, dist)

printf(res)
    
