import math

def lcm(a, b):
    return a*b//math.gcd(a, b)


x = int(input())
n = math.ceil(math.sqrt(x))

ans = 0
for i in range(1, n):
    if(x % i == 0 and lcm(x//i, x) == x):
        ans = i 

print(ans, x//ans)
