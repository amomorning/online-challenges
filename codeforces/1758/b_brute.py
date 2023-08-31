
tot = 0

def solve():
    global tot
    for i in range(1, 100):
        for j in range(1, i+1):
            for k in range(1, j+1):
                for u in range(1, k+1):
                    # if (i^j^k^u) * 4 == i+j+k+u:
                    #     print(i, j, k, u, '=', (i+j+k+u)//4)
                    #     tot += 1
                    #     if tot > 10:
                    #         return
                    for v in range(1, u+1):
                        for w in range(1, v+1):
                            if (i^j^k^u^v^w) * 6 == i+j+k+u+v+w:
                                print(i, j, k, u, v, w, '=', (i+j+k+u+v+w)//6)
                                tot += 1
                                if tot > 10:
                                    return

solve()
