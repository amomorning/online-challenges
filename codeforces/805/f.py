import random, bisect

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


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ma = Encodict(lambda: 0)
    for x in a:
        while x % 2 == 0:
            x //= 2
        if x != 1: ma[x] += 1
    
    nb = [Encodict(lambda:0) for _ in range(32)]
    for i in range(n):
        while b[i] % 2 == 0:
            b[i] //= 2
        nb[b[i].bit_length()][b[i]] += 1
        
    b = sorted(b)
    
    na = sorted(ma.keys(), reverse=True)
    cur = 31
    # print(na)
    for x in na:
        l = x.bit_length()
        while cur > l:
            for bb, v in nb[cur].items():
                while bb.bit_length() > l:
                    bb //= 2
                while bb % 2 == 0:
                    bb //= 2
                nb[bb.bit_length()][bb] += v
            nb[cur] = Encodict(lambda:0)
            cur -= 1
        
        if nb[l][x] < ma[x]:
            print("No")
            return
        else:
            nb[l][x] -= ma[x]

    print("Yes")
    # print(mp.items())

for _ in range(int(input())):
    solve()
