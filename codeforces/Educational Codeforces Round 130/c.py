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

    cnt = [[0] for _ in range(3)]
    for i in range(n):
        for j in range(3):
            cnt[j].append(cnt[j][-1])
        cnt[ord(s[i]) - ord('a')][-1] += 1

    for i, ids in enumerate(bs):
        idt = bt[i]
        printt(['ids, idt =', ids, idt])

        if ids > idt:
            printt(['cntc =', cnt[2][ids+1] - cnt[2][idt]])
            if cnt[2][ids+1] - cnt[2][idt] > 0:
                printf("NO")
                return
        elif ids < idt:
            printt(['cnta =', cnt[0][idt+1] - cnt[0][ids]])
            if cnt[0][idt+1] - cnt[0][ids] > 0:
                printf("NO")
                return

    printf("YES")
    return


    
for _ in range(int(input())):
    solve()
