import math
class PrimeTable:
    def __init__(self, n:int) -> None:
        self.n = n

        self.primes = []
        self.min_div = [0] * (n+1)
        self.min_div[1] = 1

        mu = [0] * (n+1)
        phi = [0] * (n+1)
        mu[1] = 1
        phi[1] = 1

        for i in range(2, n+1):
            if not self.min_div[i]:
                self.primes.append(i)
                self.min_div[i] = i
                mu[i] = -1
                phi[i] = i-1
            for p in self.primes:
                if i * p > n: break
                self.min_div[i*p] = p
                if i % p == 0:
                    phi[i*p] = phi[i] * p
                    break
                else:
                    mu[i*p] = -mu[i]
                    phi[i*p] = phi[i] * (p - 1)

    def is_prime(self, x:int):
        if x < 2: return False
        if x <= self.n: return self.min_div[x] == x
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0: return False
        return True
    
    def prime_factorization(self, x:int):
        for p in range(2, int(math.sqrt(x))+1):
            if x <= self.n: break
            if x % p == 0:
                cnt = 0
                while x % p == 0: cnt += 1; x //= p
                yield p, cnt
        while (1 < x and x <= self.n):
            p, cnt = self.min_div[x], 0
            while x % p == 0: cnt += 1; x //= p
            yield p, cnt
        if x >= self.n and x > 1:
            yield x, 1
    
    def get_factors(self, x:int):
        """ Not in ascending order"""
        factors = [1]
        for p, b in self.prime_factorization(x):
            n = len(factors)
            for j in range(1, b+1):
                for d in factors[:n]:
                    factors.append(d * (p ** j))
        return factors


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bits = [0] * n
    
    def ask(self, p, tot=0):
        while p < self.n: tot += self.bits[p]; p += ~p & p + 1
        return tot
    
    def add(self, p, x):
        while p >= 0: self.bits[p] += x; p -= ~p & p + 1


pt = PrimeTable(400000)
queries = []
for _ in range(int(input())):
    l, r = map(int, input().split())
    queries.append((r, l, _))

queries = sorted(queries)
fenwick = Fenwick(queries[-1][0] + 1)

def process(k):
    # print('cur =', k)
    vec = []
    for x in pt.get_factors(k+k):
        if x < k: vec.append(x)
    vec = sorted(vec)
    for p in range(len(vec)):
        val = 0
        for q in range(p+1, len(vec)):
            i, j = vec[p], vec[q]
            if k % i == 0 and k % j == 0: val += 1
            elif k < i + j : val += 1
        # print(vec[p], val)
        fenwick.add(vec[p], val)


ans = []
cur = 0
process(0)
for r, l, cas in queries:
    while cur < r:
        cur += 1
        process(cur)
    # print(fenwick.ask(l))
    ans.append((math.comb(r-l+1, 3) - fenwick.ask(l), cas))

ans = sorted(ans, key=lambda x: x[1])
print('\n'.join(map(lambda x:str(x[0]), ans)))



