import heapq, itertools
import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))
res = []
def solve(cas):
    n, k = inp()
    a = inp()

    left = [0] * (n+1)
    def check(bar):
        q = []
        s = 0
        for i in range(n):
            if s + a[i] < bar:
                heapq.heappush(q, -a[i])
                s += a[i]
            elif len(q) and -q[0] > a[i]:
                s += q[0]
                s += a[i]
                heapq.heappushpop(q, -a[i])
            left[i+1] = len(q)

        q = []
        s = 0
        for i in range(n-1, -1, -1):
            # add x to p
            if s + a[i] < bar:
                heapq.heappush(q, -a[i])
                s += a[i]
            elif len(q) and -q[0] > a[i]:
                s += q[0]
                s += a[i]
                heapq.heappushpop(q, -a[i])
            if len(q) + left[i]>= k: return True
        return False
    
    tmp = list(itertools.accumulate(sorted(a), initial=0))
    l, r = tmp[(k + 1) // 2], tmp[k] - tmp[k // 2]
    while l <= r:
        m = (l+r) >> 1
        if check(m):
            r = m-1
        else:
            l = m+1
    res.append(r)

cas = int(input())
for _ in range(cas):
    solve(_)

print(*res, sep='\n')
