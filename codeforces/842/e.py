import itertools, random
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

def sort_left(arr):
    n = 2 * len(arr) // 3
    return list(sorted(arr[:n])) + arr[n:]

def sort_right(arr):
    n = len(arr) // 3
    return arr[:n] + list(sorted(arr[n:]))

def is_sorted(arr):
    if arr == list(sorted(arr)):
        return True
    return False


n = 3
ans = Encodict(lambda : 0)
for cp in itertools.permutations(range(1, 3*n+1)):
    p = list(cp)
    tot_left = 0
    while not is_sorted(p):
        new_p = sort_left(p)
        if new_p != p:
            p = new_p 
            tot_left += 1
        new_p = sort_right(p)
        if new_p != p:
            p = new_p
            tot_left += 1

    p = list(cp)
    tot_right = 0
    while not is_sorted(p):
        new_p = sort_right(p)
        if new_p != p:
            p = new_p 
            tot_right += 1
        new_p = sort_left(p)
        if new_p != p:
            p = new_p
            tot_right += 1

    print(cp, tot_left, tot_right)
    ans[min(tot_left, tot_right)] += 1
print(ans.items())
