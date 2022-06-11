import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)


def solve():
    X, A, D, N = map(int, input().split())

    if D >= 0:
        if X <= A:
            printf(A - X)
            return
        if X >= D * (N-1) + A:
            printf(X-D * (N-1) - A)
            return
        
        L = (X-A)//D*D + A
        R = L + D
        printf(min(X-L, R-X))

        return
    else:
        if X >= A:
            printf(-A + X)
            return
        if X <= D * (N-1) + A:
            printf(-X+D * (N-1) + A)
            return
        L = (X-A)//D*D+A
        R = L + D
        printf(min(L-X, X-R))
        return
solve()

