import math
n, k = map(int, input().split())
cur = 0
ans = math.inf
for i in range(n):
    a, b = map(int, input().split())
    if k >= i+1:
        cur += a + b
        ans = min(ans, cur + b * (k-i-1))
print(ans)
