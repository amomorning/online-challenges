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
    s = input()

    cur = 0 # 0 - even; 1 - odd
    lst = cur
    cnt = 1
    tot = 0
    for i in range(1, n):
        if(s[i] != s[i-1]):

            # print("25: ", tot, cur, cnt)
        
            # if(cnt == 1):
            #     cnt = cur
            #     tot += 1
            #     i += 1
            #     lst = -1
            #     continue
            # lst = cur
            if(cur == 0):
                if(cnt % 2 == 1):
                    # print("ok")
                    cur = 1
                else:
                    cur = 0
            elif(cur == 1):
                tot += 1
                if(cnt % 2 == 1):
                    cur = 0
                else:
                    cur = 1
            # print("43: ", tot, cur, cnt)
            cnt = 0

        cnt += 1

    
    if(cur == 1):
        tot += 1
    print(">>>>:", tot, nums)
