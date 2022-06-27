import math
MOD = 998244353





def qpow(x, y, p):
    
    ans = 1
    while y:
        if y & 1:
            ans *= x
            ans %= p
        x *= x
        x %= p
        y >>= 1
    return ans
 
 
def comb(n, m, p):
    if n < m:
        return 0
    if n == m:
        return 1
    return perm[n] * inv_fact[m] * inv_fact[n-m] % p


n = int(input())

perm = [1]
inv = [1, 1]
inv_fact = [1]
for i in range(1, n*n+1):
    perm.append(perm[-1] * i % MOD)
    if i > 1:
        inv.append((MOD - MOD // i) * inv[MOD % i] % MOD)
    inv_fact.append(inv_fact[-1] * inv[i] % MOD) 
    

ans = perm[n*n]
# print(ans)
for i in range(1, n*n+1):
    
    ans -= (comb(i-1, n-1, MOD) * comb(n*n-i, n-1, MOD) * perm[n*n - 2*n + 1] * n * n * perm[n-1] * perm[n-1]% MOD) 
    ans = (ans + MOD) % MOD
        
print(ans)

