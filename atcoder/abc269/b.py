s = [input() for _ in range(10)]

flag = False
for i in range(10):
    for j in range(10):
        if s[i][j] == '#':
            if not flag:
                A, C = i, j
                flag = True
        
            B, D = i, j
print(A+1, B+1)
print(C+1, D+1)

