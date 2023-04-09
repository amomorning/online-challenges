import math
n = 6
a = [[11, 5, 9, 1, 7, 3],
     [6, 10, 2, 8, 4, 12]]

b = [[12, 5, 9, 3, 7, 1 ], [6, 10, 4, 8, 2, 11]]

ans = math.inf
for i in range(n):
    tot = []
    for j in range(0, i+1):
        tot.append(b[0][j])
    for j in range(i, n):
        tot.append(b[1][j])
    print(tot)
    cnt = 0
    for j in range(n+1):
        cnt += (-1)**j * tot[j]
    print('cnt: ', cnt)
    ans = min(ans, cnt)

print(ans)
