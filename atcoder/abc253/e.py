import sys;input=lambda:sys.stdin.readline().strip("\r\n")
import platform
LOCAL = (platform.uname().node == 'AMO')
# print(LOCAL)
def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

mod = 998244353

def solve():
    n, m, k = map(int, input().split())

    if k == 0:
        printf(pow(m, n, mod))
        return

    F = [1] * m

    def get_prefix(lst):
        res = [0]
        for x in lst:
            res.append((res[-1]+x)%mod)
        return res

    for _ in range(n-1):
        
        prefix = get_prefix(F)
        # printf(prefix)

        G = [0] * m

        for j in range(m):
            
            if j >= k: 
                G[j] += prefix[j-k+1]

            if j + k < m:
                G[j] += prefix[m] - prefix[j+k]

            G[j] %= mod
        F = G

    printf(sum(F) % mod)
    return
solve()
