import sys;input=sys.stdin.readline

for ca in range(int(input())):
    n = int(input())
    raw_s = input()

    a = input().split()[1:]
    vis = [0]*26
    for c in a:

        vis[ord(c) - ord('a')] = 1

    cur = 0
    long = 0
    for i in range(n):
        c = raw_s[i]
        # print(cur)
        if vis[ord(c) - ord('a')]:
            if long < cur:
                long = cur
            cur = 1
            continue
        cur += 1  
    
    print(long)

