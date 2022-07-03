DIV = 63
class BitSet:
    @staticmethod
    def get_bucket_size(x):
        return ((x-1) // DIV) + 1

    @staticmethod
    def popcount(x):
        x = x - ((x >> 1) & 0x5555555555555555)
        x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
        x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
        x = x + (x >> 8)
        x = x + (x >> 16)
        x = x + (x >> 32)
        return x & 0x0000007f
    

    def __init__(self, n):
        self.n = n
        self.buckets = [0] * self.get_bucket_size(n)

    def in_range(self, p):
        return 0 <= p and p < self.n

    def set(self, p, val = True):
        assert self.in_range(p)
        if val: self.buckets[p // DIV] |= 1 << (p % DIV)
        elif self.test(p): self.flip(p)
            
    def test(self, p):
        assert self.in_range(p)
        return self.buckets[p // DIV] >> (p % DIV) & 1
    
    def flip(self, p):
        assert self.in_range(p)
        self.buckets[p // DIV] ^= (p % DIV)

    def any(self):
        for mask in self.buckets:
            if mask: return True
        return False
    
    def count(self):
        ret = 0
        for mask in self.buckets:
            ret += self.popcount(mask)
        return ret
    
    def lowbit(self):
        for i, x in enumerate(self.buckets):
            if x: return (i * DIV) + (self.buckets[i] & -self.buckets[i])
    

    def resize(self, m):
        newsz = self.get_bucket_size(m)
        sz = len(self.buckets)
        if newsz < sz:
            self.buckets = self.buckets[0:sz]
        else:
            self.buckets += [0] * (newsz-sz)
        self.n = m

    def size(self):
        return self.n
    
    
    def __len__(self):
        return self.n

    
    def __and__(self, rhs):
        ret = BitSet(max(self.size(), rhs.size()))
        m = min(len(self.buckets), len(rhs.buckets))
        for i in range(m):
            ret.buckets[i] = self.buckets[i] & rhs.buckets[i]
        return ret
    
    def __or__(self, rhs):
        ret = BitSet(max(self.size(), rhs.size()))
        for i in range(len(ret.buckets)):
            if i < len(self.buckets): ret.buckets[i] |= self.buckets[i]
            if i < len(rhs.buckets): ret.buckets[i] |= rhs.buckets[i]
        return ret

    def __xor__(self, rhs):
        ret = BitSet(max(self.size(), rhs.size()))
        for i in range(len(ret.buckets)):
            if i < len(self.buckets): ret.buckets[i] ^= self.buckets[i]
            if i < len(rhs.buckets): ret.buckets[i] ^= rhs.buckets[i]
        return ret
    
    def __str__(self):
        ret = []
        for i, b in enumerate(self.buckets):
            tmp = str(bin(b))[2:][::-1]
            while len(tmp) + i * DIV < min(self.size(), (i+1)*DIV):
                tmp += '0'
            ret.append(tmp)
        return ''.join(ret)
        
n = int(input())
a = [list(map(int, list(input()))) for _ in range(n)]

bits = [BitSet(n) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j]:
            bits[i].set(j)

for b in bits:
    print(b)

tot = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i][j]:
            tot += (bits[i] & bits[j]).count()

print(tot // 3)

