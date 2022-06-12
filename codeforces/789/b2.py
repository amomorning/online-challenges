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

    n = int(input())
    s = input()
    INF = 0x3f3f3f3f
    for i, c in enumerate(s):
        ch = int(c)

        if i == 0:
            F = [[(INF, 0), (ch, 1)], [(INF, 0), (ch^1, 1)]]
            # print(F)
        else:
            G = [[(INF, 0), (INF, 0)], [(INF, 0), (INF, 0)]]

            for j in range(2):
                for k in range(2):
                    for r in range(2):
                        if(k == 1 and ch ^ r != j):
                            continue 
                        jj = ch ^ r
                        kk = k ^ 1 if jj == j else 1

                        G[jj][kk] = min(G[jj][kk], (F[j][k][0] + r, F[j][k][1] + int(ch ^ r != j)))
            F = G
            # print(F)
    res = min(F[0][0], F[1][0])
    print(res[0], res[1])
