for _ in range(int(input())):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    
    tot = 0
    for i in range(k):
        if p[i] > k:
            tot += 1

    print(tot)
