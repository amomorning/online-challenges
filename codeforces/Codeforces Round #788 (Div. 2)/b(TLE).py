import sys;input=sys.stdin.readline

def deleted_str(s, t):
    n = len(s)
    mark = [0] * n
    for i in range(1, n):
        if(s[i] in t):
            mark[i-1] = 1

    res = ''
    flag = False
    for i in range(n):
        if(mark[i] == 0):
            res += s[i]
        else:
            flag = True
    # print(mark)
    return res, flag

cas = int(input())

for ca in range(cas):
    n = int(input())
    raw_s = input()

    a = input().split()[1:]

    # print(a)

    ret, status = deleted_str(raw_s, a)

    cnt = 0
    while(status):
        
        cnt += 1
        cur_s = ret
        ret, status = deleted_str(cur_s, a)
    
    print(cnt)


