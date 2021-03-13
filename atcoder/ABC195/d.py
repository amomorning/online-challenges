n, m, q = map(int, input().split())
a = []
for i in range(n):
    w, v = map(int, input().split())
    a.append((w, v))

x = list(map(int, input().split()))

for i in range(q):
    l, r = map(int, input().split())
    cur = x[:l-1] + x[r:]
    cur = sorted(cur)

    res = 0
    vis = [False]*n
    for box in cur:
        mx = 0
        mxi = -1
        for i in range(len(a)):
            w, v = a[i]
            if(w > box or vis[i]):
                continue
            # print (w, v)
            if(v > mx):
                mxi = i
                mx = v
        if(mxi != -1):
            res += mx
            vis[mxi] = True
    print(res) 

        

