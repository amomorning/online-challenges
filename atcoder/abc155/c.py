n = int(input())

d = {}
for i in range(n): 
    s = input()
    if(d.get(s) is None):
        d[s] = 1
    else:
        d[s] = d[s] + 1

l = list(d.items())

l.sort(key=lambda x: (-x[1], x[0])) 

for k, v in l:
    if(v != l[0][1]): break
    print(k)
