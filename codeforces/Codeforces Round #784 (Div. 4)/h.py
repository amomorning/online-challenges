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



def to_list(num, lens):
    res = list(str(bin(num)))[2:]
    
    cnt_zero = lens - len(res)
    for i in range(cnt_zero):
        res.insert(0, 0)
    return list(map(int, res))


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    nums = []
    for x in a:
        nums.append(to_list(x, 31))
    
    res = 0
    for j in range(31):
        lack = n
        for i in range(n):
            lack -= nums[i][j]  
        
        # print(">>>: ", j, lack, k)
        if(lack <= k):
            if(30-j-1 < 0):
                res += 1
            else:
                res += (2 << (30-j-1))
            
            k -= lack

    printf(res)

