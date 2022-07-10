for _ in range(int(input())):
    s = input()

    vis = set()
    ans = 0
    for x in s:
        now = ord(x) - ord('a')
        vis.add(now)
        if len(vis) > 3:
            ans += 1
            vis = {now}
    if len(vis) > 0:
        ans += 1
    print(ans)
