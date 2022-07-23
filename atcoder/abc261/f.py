import random
class Encodict:
    def __init__(self, func=lambda : 0):
        self.RANDOM = random.randint(0, 1<<32)
        self.default = func
        self.dict = {}
    
    def __getitem__(self, key):
        k = self.RANDOM ^ key
        if k not in self.dict:
            self.dict[k] = self.default()
        return self.dict[k]
    
    def __setitem__(self, key, item):
        k = self.RANDOM ^ key
        self.dict[k] = item

    def keys(self):
        return [self.RANDOM ^ i for i in self.dict]
    
    def items(self):
        return [(self.RANDOM ^ i, self.dict[i]) for i in self.dict]
    
    def sorted(self, by_value=False, reverse=False):
        if by_value:
            self.dict = dict(sorted(self.dict.items(), \
                key=lambda x:x[1], reverse=reverse))
        else:
            self.dict = dict(sorted(self.dict.items(), \
                key=lambda x:self.RANDOM^x[0], reverse=reverse))

    
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bits = [0] * n
    
    def ask(self, p, tot=0):
        while p >= 0: tot += self.bits[p]; p -= ~p & p + 1
        return tot
    
    def add(self, p, x):
        while p < self.n: self.bits[p] += x; p += ~p & p + 1

    ''' k in [1, n]
    '''
    def kth(self, k):
        p, t = -1, 0
        b = self.n.bit_length()
        while ~b:
            p += 1 << b
            if p >= self.n or t + self.bits[p] >= k: 
                p -= 1 << b
            else:
                t += self.bits[p]
            b -= 1
        return -1 if p+1 >= self.n else p + 1


n = int(input())
c = list(map(int, input().split()))
x = list(map(lambda x: int(x)-1, input().split()))

mp = Encodict(list)
for i in range(n):
    mp[c[i]].append(x[i])

fen = Fenwick(n)
ans = 0
for i in range(n-1, -1, -1):
    fen.add(x[i], 1)
    ans += fen.ask(x[i]-1)
for i in mp.keys():
    m = len(mp[i])
    fen = Fenwick(m)
    tot = 0
    idx = sorted(set(mp[i]))
    mmp = Encodict(lambda: 0)
    for j, v in enumerate(idx):
        mmp[v] = j
    ls = []
    for j in range(m):
        ls.append(mmp[mp[i][j]])
        
    # print(ls) 

    for j in range(m-1, -1, -1):
        tot += fen.ask(ls[j]-1)
        fen.add(ls[j], 1)

    # print(tot) 
    ans -= tot
print(ans)

    