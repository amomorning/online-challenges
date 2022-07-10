import random
from collections import deque
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


def bfs(s, G, vis):
    q = deque()
    q.append(s)
    vis[s] = 0
    # print('Loop:', end=' ')
    while q:
        u = q.popleft()
        # print(u, end=' ')
        for v in G[u]:
            if vis[v] == -1:
                q.append(v)
                vis[v] = vis[u] ^ 1
            if vis[v] == vis[u]:
                return False
            
    # print('')

    


def solve():
    n = int(input())
    G = Encodict(list)
    for i in range(n):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
        G[b].append(a)
    
    for i in range(n):
        if len(G[i]) != 2:
            print("No")
            return 
    
    vis = [-1] * n
    for i in range(n):
        if vis[i] == -1:
            if bfs(i, G, vis) == False:
                print("No")
                return
    
    print("Yes")
        
    

for _ in range(int(input())):
    solve()
