
import math

def check(x):
    if x % math.floor(math.sqrt(x)) == 0:
        return True
    return False

eps = 1e-9

def calc(s):
    x = math.floor(math.sqrt(s))

    while x*x > s: x -= 1

    rest = s - x*x + 1


    if rest <= x:
        return 3*(x-1) + 1
    elif rest <= 2*x:
        return 3*(x-1) + 2
    else:
        return 3*(x-1) + 3

# tot = 0
# for i in range(1, 100):

#     if check(i):
#         tot += 1
#     if tot != calc(i):
#         print(i, tot, calc(i))

# print(int(1e18))

cur = int(1e18)
print(check(cur))
print(calc(cur))
print(calc(cur-2))
