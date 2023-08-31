MOD = 998244353
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    G = [[] for _ in range(n)]
    ind = [0] * n
    for i in range(m):
        u, v = map(lambda x: int(x)-1, input().split())
        G[u].append(v)
        ind[v] += 1
    
    st = set()
    for u in range(n):
        if a[u] > 0:
            st.add(u)
    tot = 0
    while st:
        subs = set()
        adds = set()
        for u in st:
            if ind[u] == 0:
                tot = (tot + a[u]) % MOD
                subs.add(u)
                for v in G[u]:
                    ind[v] -= 1
                    if v not in st:
                        adds.add(v)
                    a[v] += a[u]
                a[u] = 0

        print(subs, adds, st)
        print(a)
        st -= subs
        st |= adds
        # if len(starts) == 0:
        #     break

    print(tot)
