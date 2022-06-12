n, m = map(int, input().split())
a = [0]*m
b = [0]*m

for i in range(m):
    a[i], b[i] = map(int, input().split())

k = int(input())
c = [0]*k
d = [0]*k

for i in range(k):
    c[i], d[i] = map(int, input().split())

ans = 0

for i in range(2**k):
    s = set()
    for j in range(k):
        if(i & (1<<j)):
            s.add(d[j])
        else:
            s.add(c[j])
    cnt = 0
    for j in range(m):
        if(a[j] in s and b[j] in s):
            cnt += 1
    if(cnt > ans): ans = cnt

print(ans)
