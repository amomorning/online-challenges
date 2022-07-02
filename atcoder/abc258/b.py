n = int(input())

a = []
for i in range(n):
    a.append(list(map(int, list(input()))))


dirs = [(-1, -1), (-1, 0), (-1, 1), \
        (0, -1), (0, 1), \
        (1, -1), (1, 0), (1, 1)]
ans = 0
for i in range(n):
    for j in range(n):

        for d in dirs:
            cur = a[i][j]
            pos = (i, j)
            for k in range(n-1):
                nx, ny = (pos[0] + d[0]) % n, (pos[1] + d[1]) % n
                cur = cur*10 + a[nx][ny]
                pos = (nx, ny)

            ans = max(ans, cur)

print(ans)
                

