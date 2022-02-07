t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    flag = True
    for i in range(n):
        if(s[i] != s[n-i-1]):
            flag = False
    if(k >= 2):
        k = 1
    if(flag):
        print(max(k,1))
    else:
        print(k+1)
