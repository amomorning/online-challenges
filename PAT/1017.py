from queue import PriorityQueue

n, k = map(int, input().split())


def timestamp(t):
    return t[0]*3600+t[1]*60+t[2]


dic = {}
for i in range(n):
    t, p = input().split()
    p = int(p)
    hh, mm, ss = map(int, t.split(':'))
    dic[(hh, mm, ss)] = p

d = sorted(dic.items(), key=lambda z: z[0], reverse=False)
tot = 0
for items in d:
    if(timestamp(items[0]) < timestamp((8, 0, 0))):
        tot += timestamp((8, 0, 0)) - timestamp(items[0])
    
q = PriorityQueue()
cnt = 0
for items in d:
    ts = timestamp(items[0])
    p = items[1] * 60
    if(ts < timestamp((8, 0, 0))):
        ts = timestamp((8, 0, 0))
    if(ts > timestamp((17, 0, 0))):
        continue
    
    cnt += 1
    if(q.qsize() < k):
        q.put(ts+p)
    else:
        cur = q.get()
        if(cur > ts): 
            tot += cur - ts
            q.put(cur+p)
        else: 
            q.put(ts+p)



print(round(tot/60/cnt, 1))
