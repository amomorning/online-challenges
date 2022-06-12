n = int(input())

vis = [0]*(2*n+2)

print(1, flush=True)
vis[1] = 1
for i in range(n):
    q = int(input())
    vis[q] = 1
    for j in range(1, 2*n+2):
        if vis[j] == 0:
            print(j, flush=True)
            vis[j] = 1
            break
