mp = [[False] * 15 for _ in range(15)]

for i in range(1, 10, 2):
    for j in range(i, 15-i):
        mp[i][j] = True
        mp[j][i] = True
        mp[14-i][j] = True
        mp[j][14-i] =True
        

# for i in range(15):
#     for j in range(15):
#         print('m', end=' ') if mp[i][j] else print('o', end=' ')
#     print('')

r, c = map(int, input().split())
print('white') if mp[r-1][c-1] else print('black')


