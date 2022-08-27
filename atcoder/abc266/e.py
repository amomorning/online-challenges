N = int(input())
E = [-1] * (N+1)
E[0] = 0
for i in range(1, N+1):
    E[i] = 0
    for x in range(1, 7):
        E[i] += max(x, E[i-1]) / 6

print(E[N])
