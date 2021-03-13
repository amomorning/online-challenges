s = input()
n = int(s)

base = (len(s)-1)//3*3
    
tot = 0
for i in range(1, base//3):
    l = int('9'*(3*i))
    r = int('9'*(3*(i+1)))
    tot += (r-l)*i
    # print(l, r)

o = base//3
try:
    m = int('9'*(3*o))
    tot += (n-m)*o
    print(tot)
except ValueError:
    print(0)

