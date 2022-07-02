import itertools 
import bisect
n, q, x = map(int, input().split())
w = list(map(int, input().split()))
acc = list(itertools.accumulate(w+w))

l = 0
vis = [-1] * n
buckets = []

while vis[l] == -1:
    vis[l] = len(buckets)
    tmp = x if l == 0 else x + acc[l-1]
    r = bisect.bisect_left(acc, tmp)
    rst = 0
    if r == len(acc):
        r = bisect.bisect_left(acc, tmp%acc[-1])
        rst = tmp // acc[-1]

    buckets.append(rst * n * 2 + r-l+1)
    l = (r+1)%n

# print(buckets)
# print(vis)
pos = vis[l]
 
for _ in range(q):
    k = int(input())-1
    if k <= pos:
        print(buckets[k])
    else:
        print(buckets[ (k-pos) % (len(buckets) - pos) + pos])


