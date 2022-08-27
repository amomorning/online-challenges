mod = 998244353
n = int(input())

n = (n%mod + mod)%mod
print(n)
