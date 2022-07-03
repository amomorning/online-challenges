import random
n = 100
print(n)
for i in range(n):
    s = ''
    for j in range(n):
        s += str(random.randint(0, 1))
    print(s)
