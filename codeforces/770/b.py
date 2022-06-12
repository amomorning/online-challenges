T = int(input())

for _ in range(T):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    total = sum(a)
    if((total + x + y)%2):
        print("Bob")
    else:
        print("Alice")
