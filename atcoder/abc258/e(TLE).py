n, q, x = map(int, input().split())
w = list(map(int, input().split()))

l = 0
cur = w[0]
buckets = []
vis = [-1] * n
vis[0] = 0
for r in range(1, 10**100):
    if cur < x:
        cur += w[r%n]
    else:
        buckets.append(r-l) 
        cur = w[r%n] 
        l = r
        if vis[l%n] > -1:
            pos = vis[l%n]
            break
        vis[l%n] = len(buckets)

print(buckets)
print(vis)
for _ in range(q):
    k = int(input())-1
    if k <= pos:
        print(buckets[k])
    else:
        print(buckets[ (k-pos) % (len(buckets) - pos) + pos])


