for i in range(1, 100):
    for j in range(1, i):
        for k in range(1, j):
            for u in range(1, k):
                tmp = max([i, j, k, u]) - min([i, j, k, u])

                if tmp * tmp == i+j+k+u:
                    print(i, j, k, u)
