import sys;input=sys.stdin.readline.strip("\r\n")


def deleted_str(pos):

    flag = False
    res = set()

    for i, a in enumerate(pos):
        if(a - i - 1 > 0):
            flag = True
            res.add(a - i - 1)
    
    return res, flag

cas = int(input())

for ca in range(cas):
    n = int(input())
    raw_s = input()

    a = input().split()[1:]

    pos = []
    for i in range(1, len(raw_s)):
        if(raw_s[i] in a):
            pos.append(i)
    # print(a)
    if(len(pos) == 0):
        print(0)
        continue

    ret, status = deleted_str(pos)

    cnt = 1 
    while(status):
        cnt += 1
        pos = ret
        ret, status = deleted_str(pos)
    
    print(cnt)
