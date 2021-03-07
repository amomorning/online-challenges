# A+B for Polynomials 


d = {}
for i in range(2):
    raw = input().split()
    for j in range(1, len(raw)):
        if j % 2 == 1:
            try: 
                d[int(raw[j])] += float(raw[j+1])
            except KeyError:
                d[int(raw[j])] = float(raw[j+1])

dic = sorted(d.items(), key=lambda z: z[0], reverse=True)
lst = []
for d in dic:
    if(d[1] != 0):
        lst.append('{} {}'.format(d[0], round(d[1],1)))

if(len(lst) == 0):
    print('0')
else:
    print(len(lst)," ".join(lst))
