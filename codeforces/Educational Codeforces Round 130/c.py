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
    
    cas = []
    cat = []
    bs = []
    bt = []
    
    for i in range(n):
        if s[i] != 'b':
            cas.append(s[i])
        else:
            bs.append(i)
        if t[i] != 'b':
            cat.append(t[i])
        else:
            bt.append(i)
    
    if cas != cat:
        printf("NO")
        return

    cntc = [0]
    cnta = [0]
    for i in range(n):
        if s[i] == 'c':
            cntc.append(cntc[-1] + 1)
            cnta.append(cnta[-1])
        elif s[i] == 'a':
            cnta.append(cnta[-1] + 1)
            cntc.append(cntc[-1])
        else:
            cntc.append(cntc[-1])
            cnta.append(cnta[-1])

    for i, ids in enumerate(bs):
        idt = bt[i]
        printt(['ids, idt =', ids, idt])

        if ids > idt:
            printt(['cntc =', cntc[ids+1] - cntc[idt]])
            if cntc[ids+1] - cntc[idt] > 0:
                printf("NO")
                return
        elif ids < idt:
            printt(['cnta =', cnta[idt+1] - cnta[ids]])
            if cnta[idt+1] - cnta[ids] > 0:
                printf("NO")
                return

    printf("YES")
    return


    
for _ in range(int(input())):
    solve()
