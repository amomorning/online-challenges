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


n, x = map(int, input().split())
cnt = 0

def calclen(x):
    a = list(str(x))
    mx = int(max(a))
    return len(str(x * mx))

def solve(n, x):
    global cnt

    
    a = list(str(x))
    mxlen = len(a)
    sa = set(a)
    if len(sa) == 1 and a[0] == '1' and n > mxlen:
        return False
    
    if mxlen > n:
        return False

    candidates = [x]
    mxnextlen = mxlen

    while mxlen < n:
        # printf(len(candidates))
        for c in candidates:
            a = list(str(c))
            for i in range(2, 10):
                if str(i) in a:
                    mxnextlen = max(mxnextlen, calclen(c * i))
                    mxlen = max(mxlen, len(str(c * i)))

        newcand = []
        for c in candidates:
            a = list(str(c))
            for i in range(2, 10):
                if str(i) in a and (len(str(c * i)) == mxlen or calclen(c * i) == mxnextlen):
                    newcand.append(i*c)


        # printf(newcand)
        candidates = newcand
        cnt += 1

    return True

printf(cnt) if solve(n, x) else printf(-1)
