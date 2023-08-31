def check(a, b, c):
    return (a^b) + (b^c) + (a^c)

for _ in range(int(input())):
    n = int(input())

    if n % 2 == 0:
        print(0, 0, n//2)
    else:
        print(-1)

