
def ask(i):
    print('?', i, flush=True)
    return int(input())

def answer(i):
    print('!', i, flush=True)

n = int(input())

l, r = 1, n+1
while l <= r:  
    m = (l+r) >> 1
    if ask(m) == 0:
        ans = m
        l = m+1
    else:
        r = m-1
answer(ans)
