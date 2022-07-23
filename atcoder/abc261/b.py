n = int(input())

a = []
for i in range(n):
    a.append(input())

flag = True
for i in range(n):
    for j in range(i):
        if a[i][j] != a[j][i]:
            if a[i][j] == 'D' or a[j][i] == 'D':
                flag = False
        else:
            if a[i][j] == 'W' or a[j][i] == 'W':
                flag = False
            if a[i][j] == 'L' or a[j][i] == 'L':
                flag = False

print('correct') if flag else print('incorrect')

        
