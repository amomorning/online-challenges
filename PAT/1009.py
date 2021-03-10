a = {}
raw = input().split()
for i in range(len(raw)):
    if(i%2 == 1):
        try:
            a[int(raw[i])] += float(raw[i+1])
        except KeyError:
            a[int(raw[i])] = float(raw[i+1])
b = {}
raw = input().split()
for i in range(len(raw)):
    if(i%2 == 1):
        try:
            b[int(raw[i])] += float(raw[i+1])
        except KeyError:
            b[int(raw[i])] = float(raw[i+1])

c = {}
for i in a.keys():
    for j in b.keys():
        try:
            c[i+j] += a[i] * b[j]
        except KeyError:
            c[i+j] = a[i] * b[j]

dic = sorted(c.items(), key=lambda z: z[0], reverse=True)
lst = []
for d in dic:
    if(d[1] != 0):
        lst.append('{} {}'.format(d[0], round(d[1],1)))

if(len(lst) == 0):
    print('0')
else:
    print(len(lst)," ".join(lst))
