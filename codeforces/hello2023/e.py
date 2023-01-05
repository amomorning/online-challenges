def ask(ix, n):
    s = list('1'*n)
    s[ix] = '0'
    print('?', ix+1, ''.join(s), flush=True)
    return int(input())

def ask_candidate(arr, ix, n):
    s = list('0'*n)
    for i in arr:
        s[i] = '1'
    print('?', ix+1, ''.join(s), flush=True)
    return int(input())

def answer(arr, n):
    s = list('0'*n)
    for i in arr:
        s[i] = '1'
    print('!', ''.join(s), flush=True)


n = int(input())
deg = []
for i in range(n):
    deg.append(ask(i, n))

odeg = sorted(zip(deg, range(n)), reverse=True, key=lambda x:x[0])
# print(odeg)

arr = set([odeg[0][1]])
cur = odeg[0][0]
for i in range(1, n):
    d, ix = odeg[i]
    if d == cur:
        arr.add(ix)
        continue
    if ask_candidate(arr, ix, n) > 0:
        for j in range(i+1):
            arr.add(odeg[j][1])
        cur = d

# print(arr)
answer(arr, n)


