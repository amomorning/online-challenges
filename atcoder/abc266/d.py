N = int(input())
T, X, A = [0], [0], [0]
M = 5
for i in range(N):
    t, x, a = map(int, input().split())
    T.append(t); X.append(x); A.append(a)
dp = [[-1]*M for _ in range(N+1)]

dp[0][0] = 0
for i in range(1, N+1):
    for j in range(M):
        for k in range(M):
            if dp[i-1][k] == -1: continue
            if abs(k-j) > T[i] - T[i-1]: continue
            dp[i][j] = max(dp[i][j], dp[i-1][k] + A[i] * int(j == X[i]))

print(max(dp[N]))
