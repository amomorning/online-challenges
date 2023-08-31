import math
for _ in range(int(input())):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))

    G = [[] for _ in range(n)]
    tot = 0
    for i in range(m):
        u, v = map(lambda x: int(x)-1, input().split())
        tot += 1
        G[u].append(v)
        G[v].append(u)
    
    if tot % 2 == 1:
        ans = math.inf
        for u, weight in enumerate(w):
            if len(G[u]) % 2 == 1:
                ans = min(ans, weight)
            else:
                for v in G[u]:
                    if len(G[v]) % 2 == 0:
                        ans = min(ans, weight+w[v])
        print(ans)
    else:
        print(0)
                
        
    
        

        
    

