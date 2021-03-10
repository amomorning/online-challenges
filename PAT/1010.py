## WA at test 0

n1, n2, tag, rad = input().split()
tag = int(tag)
rad = int(rad)

d = {}
for i in range(10, 36):
    d[chr(i+87)] = i
for i in range(10):
    d[str(i)] = i

def base(val, rad):
    bas = 1
    tot = 0
    for c in val[::-1]:
        tot += d[c]*bas
        bas *= rad
    return tot

def maxv(val):
    mx = 0
    for c in val:
        mx = max(mx, d[c])
    return mx

        
res = 'Impossible'
if(tag == 1):
    ans = base(n1, rad)
    l = maxv(n2)
    r = max(l, ans)
    while(l <= r):
        m = (l+r) >> 1 
        if(base(n2, m) > ans): 
            r = m-1
        elif(base(n2, m) == ans):
            res = m
            break
        else:
            l = m+1

else:
    ans = base(n2, rad)
    l = maxv(n1)
    r = max(l, ans)
    while(l <= r):
        m = (l+r) >> 1 
        if(base(n1, m) > ans): 
            r = m-1
        elif(base(n1, m) == ans):
            res = m
            break
        else:
            l = m+1


print(res)
