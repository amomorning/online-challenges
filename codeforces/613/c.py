import math

def lcm(a, b):
    # print(a, b)
    # print(math.gcd(a, b))
    # print(a*b//math.gcd(a, b))
    return a*b//math.gcd(a, b)


x = int(input())
n = math.ceil(math.sqrt(x))

ans = 1
for i in range(1, n):
    if(x % i == 0 and lcm(x//i, i) == x):
        ans = i 

print(ans, x//ans)
