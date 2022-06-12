import sys;input=sys.stdin.readline

cas = int(input())

for ca in range(cas):
    n = int(input())
    a = map(int, input().split())

    mp = {}
    for i in range(n+1):
        mp[i] = 0
    flag = False

    for x in a:
        mp[x] += 1
        if(mp[x] >= 3):
            flag = True
            res = x
            break

    if(flag):print(res)
    else: print(-1)
             
