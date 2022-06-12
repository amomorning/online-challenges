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
    n, k = map(int, input().split())
    s = input()

    tot = 0
    for i in range(n-1):
        tot += int(s[i]+s[i+1])
    markmove = -1

    for i in range(n-1, -1, -1):
        if s[i] == '1':
            
            if n-i-1 <= k and n-i-1 > 0:
                k -= n-i-1
                tot -= 10
                markmove = i
                if i == 0:
                    tot += 1
                
            break

    for i in range(n):
        if s[i] == '1':
            if i > 0 and i <= k and i != markmove and i != n-1:
                k -= i
                tot -= 1
            break

    printf(tot)
