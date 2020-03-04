t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a, b = 1, 2
    sum = 2
    for i in range(100):
        c = a + b
        if(c > n):
            break
        if(c%2 == 0):
            sum += c
        a = b
        b = c
    print(sum)

        
