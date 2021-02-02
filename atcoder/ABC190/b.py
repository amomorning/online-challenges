n, s, d = map(int, input().split())

flag = False

for i in range(n):
    x, y = map(int, input().split())
    if ( y <= d ) : continue
    if ( x >= s ) : continue
    flag = True

if(flag): print('Yes')
else: print('No')
