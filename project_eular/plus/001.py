t = int(input())
for i in range(t):
    n = int(input())
    sum = 0
    for i in range(n):
        if(i%3 == 0 or i%5 == 0): 
            sum += i
    print(sum)
