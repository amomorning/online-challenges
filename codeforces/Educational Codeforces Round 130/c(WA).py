import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printt(a):
    if LOCAL:
        print('(test)', end=' ')
        printf(a)

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)


def solve():
    n = int(input())
    s = list(input())
    t = list(input())
    for i in range(n-1):
        if s[i] != t[i]:
            if s[i] == 'a' and t[i] == 'b':
                idx = i + 1
                while idx < n-1 and s[idx] != 'b':
                    idx += 1
                
                if s[idx] == 'b':
                    for j in range(idx, i, -1):
                        s[j], s[j-1] = s[j-1], s[j]
                else:
                    printf("NO")
                    return
            elif s[i] == 'b' and t[i] == 'c':
                idx = i + 1
                while idx < n-1 and s[idx] == 'b':
                    idx += 1
                if s[idx] == 'c':
                    s[i] = 'c'
                    s[idx] = 'b'
                else:
                    printf("NO")
                    return
            else:
                printf("NO")
                return

    printt(s)
    printt(t)

    if s == t:
        printf("YES")
    else:
        printf("NO")


for _ in range(int(input())):
    solve()
