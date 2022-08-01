
def check(a, b, m):
    l = 0
    for i in range(m):
        if a[i] == b[i]: continue
        elif a[i] > b[i]:
            delta = a[i] - b[i]
            b[i] += delta
            b[i+1] -= delta
            l += delta
        elif a[i] < b[i]:
            delta = b[i] - a[i]
            b[i] -= delta
            b[i+1] += delta
            l -= delta
            
    return l


for _ in range(int(input())):
    n, m = map(int, input().split())

    l = []
    for i in range(n):
        a = list(map(int, input().split()))
        l.append(a)
    
    cnt = 0
    for i in range(1, n):
        tmp = check(l[0], l[i], m)
        if tmp == 0:
            cnt += 1
        else:
            k = i
            ans = tmp
            
        # print(check(l[0], l[i], m))
    # print('cnt =', cnt)
    if cnt == n-2:
        print(k+1, ans)
        continue
    
        
    print(1, -ans)
    


