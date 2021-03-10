tot = 1

name = ['W', 'T', 'L']
res = ''
for i in range(3):
    a = list(map(float, input().split()))
    mx = max(a)
    res += name[a.index(mx)] + ' '
    tot *= max(a)
    
print("{}{}".format(res, round((tot*0.65 -1) * 2, 2)))
