import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    mp = {}
    for i in range(10):
        mp[i] = 0
    for i in range(n):
        tmp = a[i] % 10
        mp[tmp] += 1

    flag = False
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if (i+j+k) % 10 == 3:
                    mp[i] -= 1
                    mp[j] -= 1
                    mp[k] -= 1

                    if mp[i] >= 0 and mp[j] >= 0 and mp[k] >= 0:
                        # print(i, j, k)
                        flag = True
                    mp[i] += 1
                    mp[j] += 1
                    mp[k] += 1
                        
    printf("YES") if flag else printf("NO")
                    
                    

