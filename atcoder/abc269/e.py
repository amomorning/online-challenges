
def ask_row(l, r):
    print('?', l, r, 1, n, flush=True)
    return int(input())

def ask_column(l, r):
    print('?', 1, n, l, r, flush=True)
    return int(input())

n = int(input())
l, r = 1, n
while l <= r:
    m = (l + r) >> 1
    if ask_row(l, m) == m-l+1:
        l = m+1
    else:
        x = m
        r = m-1

l, r = 1, n
while l <= r:
    m = (l + r) >> 1
    if ask_column(l, m) == m-l+1:
        l = m+1
    else:
        y = m
        r = m-1

print('!', x, y, flush=True)

