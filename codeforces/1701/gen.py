import itertools, random
t = 100
n = 8
print(t)
for _ in range(t):
    print(n)
    ans = []
    for p in itertools.permutations(range(1, n+1), n):
        x = random.randint(1, 1000)
        if x == 50:
            for i in range(n):
                ans.append((i+1)//p[i])
            break
            

    
    print(' '.join(map(str, ans)))
