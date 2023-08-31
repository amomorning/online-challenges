for _ in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    if a == 1 and b == 1 and c == 1 and d == 1:
        print(2)
    elif a == 0 and b == 0 and c == 0 and d == 0:
        print(0)
    else:
        print(1)
