n, c = map(int, input().split())

cur = [0] * 32
for i in range(32):
    if c & (1 << i):
        cur[i] = 1

T = [[0] * 32, [1] * 32]

for i in range(n):
    op, y = map(int, input().split())
    
    x = [0] * 32
    for j in range(32):
        if y & (1 << j):
            x[j] = 1
    for k in range(2):
        for j in range(32):
            if op == 1:
                T[k][j] &= x[j]
            if op == 2:
                T[k][j] |= x[j]
            if op == 3:
                T[k][j] ^= x[j]
    for j in range(32):
        cur[j] = T[cur[j]][j]
        
    # print(cur)
    ans = ''
    for j in range(31, -1, -1):
        ans += str(cur[j])
    print(int(ans, 2))
    
