import random
print(10)

for _ in range(10):
    n = random.randint(1, 10)
    m = random.randint(1, n)
    print(n, m)

    a = []
    for i in range(n):
        x = random.randint(1, 10)
        a.append(x%2)
    print(' '.join(map(str, a)))
        
