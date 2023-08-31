N = 100
P = 100000
for n in range(N):
    for x in range(n):
        flag = False
        for i in range(P):
            if (x + (i+1)*i//2) % n == 0:
                if i >= N:
                    print(n, x, i)
                flag = True
                break
        # if not flag:
        #     print(n, x)
                

