
n, m = map(int, input().split())

g = [[0]*n for i in range(n)]
for i in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u][v] = 1
    g[v][u] = 1

tot = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if g[i][j] == 1 and g[j][k] == 1 and g[i][k] == 1:
                tot += 1

print(tot)
    