n = int(input())
a = list(map(lambda x: int(x), input().split()))
flag = True
for i in a:
    if(i%2 != 0): continue
    if(i%3 != 0 and i%5 != 0): flag = False

if(flag): print('APPROVED')
else:print('DENIED')
