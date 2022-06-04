import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

n, k = map(int, input().split())
a = list(map(int, input().split()))

groups = [[] for _ in range(k)]
for i in range(k):
    for j in range((n - i) // k + 1):
        if i + k * j < n:
            groups[i].append(a[i + k * j ])

b = [0] * n
for i, g in enumerate(groups):
    g = sorted(g)
    for j, it in enumerate(g):
        b[i + k * j] = it

flag = True
for i in range(1, n):
    if b[i] < b[i-1]:
        flag = False
printf('Yes') if flag else printf('No')
# print(groups)
