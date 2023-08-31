def ask_interval(l, r):
    print('?', l, r, flush=True)
    return set(map(int, input().split()))

def solve():
    n = int(input())

    ans = set(range(1, n+1))

    while len(ans) > 1:
        st = sorted(ans)
        l = st[0]
        r = st[len(st) // 2]
        
        ret = ask_interval(l, r)
        raw = set(range(l, r+1))
        
        if ret == raw and len(ret) == 1:
            print('!', list(ret)[0], flush=True)
            return

        if len(ret & raw) % 2 == 0:
            ans -= ret
            ans -= raw
        else:
            ans = ret & raw

        # print(ans, ret&raw, ret^raw)

    print('!', list(ans)[0], flush=True)
    return


for _ in range(int(input())):
    solve()
