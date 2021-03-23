# TLE

import bisect
n, k = map(int, input().split())

a = []
for i in range(n):
    a.append(int(input()))

dp = [(-1, a[n-1])]
for i in range(n-2, -1, -1):
    for item in dp:
        if(item[1] >= a[i] - k and item[1] <= a[i] + k):
            bisect.insort_left(dp, (item[0]-1, a[i])) 
            # print(dp)
            break

res = 0
for i in dp:
    res = min(res, i[0])
print(-res)

