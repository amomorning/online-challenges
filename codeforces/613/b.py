def check(a):
    sum = 0
    for i in a:
        sum += i
        if(sum <= 0): return False
    
    sum = 0
    for i in reversed(a):
        sum += i
        if(sum <= 0): return False
    return True



t = int(input())
for tt in range(t):
    n = int(input())
    a = list(map(lambda x: int(x), input().split()))
    if(check(a)):
        print('YES')
    else: 
        print('NO')
