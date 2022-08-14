for _ in range(int(input())):
    n = int(input())

    a = [0] * n 
    if n % 2 == 0:
        for i in range(0, n, 2):
            a[i] = i+2
        for i in range(1, n, 2):
            a[i] = i
    else:
        a[0] = 1
        for i in range(2, n, 2):
            a[i] = i
        for i in range(1, n, 2):
            a[i] = i+2
    print(' '.join(map(str, a)))
    
