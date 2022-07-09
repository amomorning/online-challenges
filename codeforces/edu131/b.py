
for _ in range(int(input())):
    n = int(input())

    vis = [0] * (n+1)
    ans = []
    for i in range(1, n+1):
        if vis[i] == 0:
            p = i
            while(p <= n):
                ans.append(p)
                vis[p] = 1
                p *= 2
    print(2)
    print(' '.join(map(str, ans))) 
                
        
