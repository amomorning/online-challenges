import itertools

n = 4
ans = (0, 0)
for p in itertools.permutations(range(1, n+1), n):
    for d in range(1, n+1):
        tot = 0
        for x, y in zip(p, p[1:]):
            if x * d == y:
                tot += 1
        ans = max(ans, (tot, d))
        if tot == 5:
            print(p)
print(ans)
