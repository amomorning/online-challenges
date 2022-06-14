for _ in range(int(input())):
    input()
    s = []
    for i in range(8):
        s.append(input())

    for i in range(1, 7):
        for j in range(1, 7):
            if s[i][j] == '#' \
                and s[i-1][j-1] == '#' \
                and s[i+1][j-1] == '#' \
                and s[i+1][j+1] == '#' \
                and s[i-1][j+1] == '#':
                print(i+1, j+1)
