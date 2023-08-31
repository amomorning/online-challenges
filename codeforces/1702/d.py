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

for _ in range(int(input())):
    s = input()
    p = int(input())
    mp = Encodict(list)
    for i, x in enumerate(s):
        mp[ord(x) - ord('a')].append(i)
        
    cur = 0 
    # print(mp.items())
    num, curi = 0, 0
    for i in range(26):
        if len(mp[i]) * (i+1) + cur <= p:
            cur += len(mp[i]) * (i+1)
            curi = i
            num = len(mp[i])
        else:
            num = (p - cur) // (i+1)
            curi = i
            break

    ans = []
    for i in range(curi):
        for pos in mp[i]:
            ans.append((pos, chr(i + ord('a'))))
    for i in range(num):
        pos = mp[curi][i]
        ans.append((pos, chr(curi + ord('a'))))
    
    ans = sorted(ans)
    print(''.join(map(lambda x: x[1], ans)))

