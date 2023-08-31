
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input()
    b = input()
    cur = 0
    while cur > -len(b) and a[cur-1] == b[cur-1]:
        cur -= 1
    if cur < 0:
        a = a[:cur]
        b = b[:cur]

    if len(b) == 0:
        print("YES")
    elif len(b) == 1:
        flag = False
        for c in a:
            if c == b[0]:
                flag = True
        print("YES") if flag else print("NO")
    else:
        print("NO")
    