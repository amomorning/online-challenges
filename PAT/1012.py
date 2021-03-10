N, M = map(int, input().split())

dic = {}
c, m, e, av = [], [], [], []
for i in range(N):
    sid, *a = map(int, input().split())
    ave = round(sum(a)/len(a))
    b = [ave, a[0], a[1], a[2]]
    dic[sid] = b

    av.append(b[0])
    c.append(b[1])
    m.append(b[2])
    e.append(b[3])

av = sorted(av, reverse=True)
c = sorted(c, reverse=True)
m = sorted(m, reverse=True)
e = sorted(e, reverse=True)

name = ['A', 'C', 'M', 'E']

for i in range(M):
    sid = int(input())
    try:
        b = dic[sid]
        idx = [av.index(b[0]), 
                c.index(b[1]),
                m.index(b[2]),
                e.index(b[3])]
            
        # print(b)
        # print(idx)
        print(min(idx)+1, name[idx.index(min(idx))])

    except KeyError:
        print('N/A')
    
