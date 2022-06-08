import sys; input = lambda:sys.stdin.readline().strip("\r\n")


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    tot = 0
    b = [0]*k
    
    for i in range(n):
        tot += a[i]//k
        if a[i] % k != 0:
            b[a[i]%k] += 1
    
    vis = [0]*k
    for i in range(k):
        if vis[i] == 1:
            continue
        
        left = k-i
        if left <= i:
            tot += b[i] // 2
            b[i] = b[i] % 2
            left = i + 1

        while b[i] > 0 and left < k:
            if vis[left] == 1:
                left += 1
                continue
            num = min(b[left], b[i])
            b[i] -= num
            b[left] -= num
            tot += num

            if b[left] == 0:
                vis[left] = 1

            left += 1
                
        vis[i] = 1 
        

    print(tot)
                

        
