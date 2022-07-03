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
    
    def flip(self, p = None):
        if p is None:
            for i in range(self.n):
                self.flip(i)
        else:
            assert self.in_range(p)
            self.buckets[p // DIV] ^= 1 << (p % DIV)

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
            if x > 0: return (i * DIV) + (x & -x).bit_length()-1
    
    def touch(self, l, r):
        L, R = l // DIV, r // DIV
        for i in range(DIV):
            if (self.buckets[L] >> i) & 1:
                w = L * DIV + i
                if l <= w and w <= r: return w
        for i, x in enumerate(self.buckets[L+1, R]):
            if x: return i * DIV + (x & -x).bit_length() - 1
        for i in range(DIV):
            if (self.buckets[R] >> i) & i:
                w = R * DIV + i
                if l <= w and w <= r: return w
        return -1

    def resize(self, m):
        newsz = self.get_bucket_size(m)
        sz = len(self.buckets)
        if newsz < sz:
            self.buckets = self.buckets[0:sz]
        else:
            self.buckets += [0] * (newsz-sz)
        self.n = m
        return None

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
    
    def __invert__(self):
        self.flip()
    
    def __ilshift__(self, m):
        p, w = m // DIV, m % DIV
        for i in range(len(self.buckets)-1, -1, -1):
            if w == 0:
                self.buckets[i] = 0 if i-p < 0 else self.buckets[i-p] 
            else:
                a = 0 if i-p-1 < 0 else self.buckets[i-p-1] >> (DIV - w) 
                b = 0 if i-p < 0 else self.buckets[i-p] << w 
                self.buckets[i] = (a | b) % (1 << DIV)
        return self
    
    def __irshift__(self, m):
        p, w = m // DIV, m % DIV
        n = len(self.buckets)
        for i in range(n):
            a = self.buckets[i+p] >> w if i + p < n else 0
            b = self.buckets[i+p+1] << (DIV - w) if i+p+1 < n and w > 0 else 0
            self.buckets[i] = (a | b) % (1 << DIV)
        return self
            
    
    def __str__(self):
        ret = []
        for i, b in enumerate(self.buckets):
            tmp = str(bin(b))[2:][::-1]
            while len(tmp) + i * DIV < min(self.n, (i+1)*DIV):
                tmp += '0'
            ret.append(tmp)
        return ''.join(ret)
    
    def __getitem__(self, p):
        return self.test(p)
    
    def __setitem__(self, p, v):
        self.set(p, v)
        
    def __hash__(self):
        return hash(tuple(self.buckets))
    
    def __iter__(self):
        return iter(tuple(self.buckets))

n = int(input())
a = [list(map(int, list(input()))) for _ in range(n)]

bits = [BitSet(n) for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if a[i][j]:
            bits[i].set(j)
            bits[j].set(i)

tot = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i][j]:
            for x, y in zip(bits[i].buckets, bits[j].buckets):
                tot += BitSet.popcount(x & y)

print(tot // 3)

