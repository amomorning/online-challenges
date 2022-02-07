for _ in range(int(input())):
    n, k = map(int, input().split())
    if (k == 1):
        print("YES")
        for i in range(n):
            print( i+1 )
        continue
    
    if(n % 2 == 1):
        print("NO")
        continue

    print("YES")
    for i in range(n):
        for j in range(k):
            print( i + 1 + j * n, end=" ")
        print("")
