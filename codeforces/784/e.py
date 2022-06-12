
import sys;input=lambda:sys.stdin.readline().strip("\r\n")
import platform
LOCAL = (platform.uname().node == 'AMO')
# print(LOCAL)
def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)


for _ in range(int(input())):
    n = int(input())

    mp = {}
    mp_bak = {}
    for u in 'abcdefghijk':
        mp[u] = {}
        for v in 'abcdefghijk':
            mp[u][v] = 0
    
    for u in 'abcdefghijk':
        mp_bak[u] = {}
        for v in 'abcdefghijk':
            mp_bak[u][v] = 0
    
    

    for i in range(n):
        s = input()
        mp[s[0]][s[1]] += 1
        mp_bak[s[1]][s[0]] += 1
    
    tot = 0
    for i in 'abcdefghijk':
        for j in 'abcdefghijk':
            for k in 'abcdefghijk':
                if(j == k): continue
                tot += mp[i][j] * mp[i][k]
                tot += mp_bak[i][j] * mp_bak[i][k]
        
    printf(tot//2)
        

