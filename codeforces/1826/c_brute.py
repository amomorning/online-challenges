
def max_count(a, m):
    cnt = [0] * (m+1)
    for x in a:
        cnt[x] += 1
    mx = max(cnt)
    ret = []
    for i in range(1, m+1):
        if cnt[i] == mx:
            ret.append(i)
    return ret
    

ans = [-1] * 100

n = 9
for m in range(1, 100):
    flag = True
    for i in range(1, m+1):
        for j in range(1, m+1):
            for k in range(1, m+1):
                for x in range(1, m+1):
                    for y in range(1, m+1):
                        for z in range(1, m+1):
                            for w in range(1, m+1):
                                for u in range(1, m+1):
                                    for v in range(1, m+1):
                                        ret = max_count([i, j, k, x, y, z, w, u, v], m)
                                        if len(ret) != 1 and ans[len(ret)] == -1:
                                            flag = False
                            
                            
    if flag == True:
        print(n, m)
        ans[m] = 1

                




