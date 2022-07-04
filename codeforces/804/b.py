
for _ in range(int(input())):
    n, m = map(int, input().split())

    a = [[0]*m for _ in range(n)]

    for i in range(n//2):
        for j in range(m//2):
            if (i+j) % 2 == 0:
                a[i*2][j*2] = 1
                a[i*2+1][j*2+1] = 1
            else:
                a[i*2+1][j*2] = 1
                a[i*2][j*2+1] = 1

    for x in a:
        print(' '.join(map(str, x)))
