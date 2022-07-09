
def check(a, n, ans):
    vis = [0] * (n)
    cnt = 0
    for x in a:
        if vis[x] < ans:
            vis[x] += 1
            continue
        cnt += 1
    for i in range(n):
        while vis[i] + 2 <= ans:
            vis[i] += 2
            cnt -= 1
        if cnt <= 0:
            return True
    return False
        


for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(lambda x:int(x)-1, input().split()))

    l, r = 1, m*2
    ans = 0
    while l <= r:
        mid = (l + r) >> 1
        if check(a, n, mid):
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
        
    print(ans) 
        

    
