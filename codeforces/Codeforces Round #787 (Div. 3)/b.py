t = int(input())

while(t > 0):
    t -= 1

    n = int(input())
    a = list(map(int, input().split()))

    flag = True
    tot = 0
    for i in range(n-2, -1, -1):
        if(a[i+1] == 0):
            flag = False
            break
        while(a[i] >= a[i+1]):
            tot += 1
            a[i] = a[i]//2

    if(flag):
        print(tot)
    else:
        print(-1)
