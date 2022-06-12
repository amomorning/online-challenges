t = int(input())

while(t > 0): 
    t -= 1
    a, b, c, x, y = map(int, input().split())

    resX = max(0, x - a)
    resY = max(0, y - b)
    if(resX + resY > c):
        print('NO')
    else: 
        print('YES')
