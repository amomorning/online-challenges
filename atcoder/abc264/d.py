mp = dict(zip('atcoder', range(7)))
s = list(map(lambda x: mp[x], list(input())))

tot = 0
for i in range(len(s)):
    for j in range(i):
        if s[j] > s[i]:
            tot += 1
print(tot)

