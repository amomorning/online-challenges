import random, math
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


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mp = Encodict(list)
    for i, x in enumerate(a):
        mp[x].append(i)
    
    tot = len(mp.keys())
    cur = math.inf 
    i = n-1
    while i >= 0:
        x = a[i]
        # print('x=', x)
        if x > cur: break
        if len(mp[x]) != mp[x][-1] - mp[x][0] + 1:
            break
        tot -= 1
        cur = x
        i -= len(mp[x])

    print(tot)

