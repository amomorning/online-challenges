n, m = map(int, input().split())
a = list(map(int, input().split()))
c = [0] * (n+1)
for i in range(m):
    x, y = map(int, input().split())
    c[x] = y

F = [0, a[0]+c[1]]

for i in range(1, n):
    G = [0] * (len(F)+1)
    mx = 0
    for j, u in enumerate(F):
        mx = max(mx, u)
        G[j+1] = F[j] + a[i] + c[j+1]
    G[0] = mx
    F = G
    

ans = 0
for i, u in enumerate(F):
    ans = max(ans, u)

print(ans)



