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
    n, m = map(int, input().split())

    flag = True
    dfs = []
    olds = []
    for i in range(n):
        a = list(map(int, input().split()))
        olds.append(a)
        if dfs == []:
            sa = sorted(a)
            for j in range(m):
                if(sa[j] != a[j]):
                    dfs.append(j)
            
            if len(dfs) == 2:
                for j in range(i):
                    if olds[j][dfs[0]] != olds[j][dfs[1]]:
                        flag = False
            
            if len(dfs) > 2:
                flag = False
        elif flag == True:
            sa = sorted(a)
            a[dfs[0]], a[dfs[1]] = a[dfs[1]], a[dfs[0]]

            for j in range(m):
                if(sa[j] != a[j]):
                    flag = False
                    break

    
    if len(dfs) == 0:
        res = [1, 1]
    else:
        res = [dfs[0]+1, dfs[1]+1]
    
    printf(res) if flag == True else printf(-1)
                    
                
                
                

