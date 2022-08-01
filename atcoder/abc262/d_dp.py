MOD = 998244353
def norm(v):
    v = v % MOD
    if v < 0: v += MOD
    return v

n = int(input())
a = list(map(int, input().split()))

tot = 0
for m in range(1, n+1):
    dp = [[0]*(m) for _ in range(m+1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(min(m-1, i), -1, -1):
            for k in range(m):
                if dp[j][k] > 0:
                    dp[j+1][(k + a[i]) % m] = (dp[j+1][(k + a[i]) % m] + dp[j][k]) % MOD
    
    tot = (tot + dp[m][0])%MOD
print(norm(tot))
    



