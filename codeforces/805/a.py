for _ in range(int(input())):
    n = int(input())
    now = 1
    while now*10 <= n:
        now *= 10
    print(n - now)
