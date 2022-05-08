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

    s = ['']*n
    for i in range(n):
        s[i] = input() 
    

    res = list(map(lambda x:list(x.replace('*', '.')), s))
    res.append(['o']*m)

    for i in range(n+1):
        for j in range(m):
            if(res[i][j] == 'o'):
                cnt = 0
                for k in range(i-1, -1, -1):
                    if(s[k][j] == 'o'):
                        break
                    if(s[k][j] == '*'):
                        cnt += 1
                
                for k in range(i-1, i-cnt-1, -1):
                    res[k][j] = '*'

    # printf('')
    for i in range(n):
        print(''.join(res[i]))
