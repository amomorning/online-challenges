
def ask_char(i):
    print("? 1", i+1, flush=True)
    return input()

def ask_inteval(l, r):
    print("? 2", l+1, r+1, flush=True)
    return int(input())

mx_pos = {}
n = int(input())
s = ask_char(0)
mx_pos[s[0]] = 0

last = 1
for i in range(1, n):
    now = ask_inteval(0, i)
    if now > last:
        ch = ask_char(i)
        s += ch
        last = now
        mx_pos[ch[0]] = i
        continue

    keys = sorted(mx_pos, key=lambda x: mx_pos[x])
    ans = ''
    l, r = 0, len(mx_pos)-1
    while l <= r:
        m = (l + r) >> 1
        cnt = ask_inteval(mx_pos[keys[m]], i)
        if cnt + m == now:
            l = m+1
            ans = keys[m]
        else:
            r = m-1
    
    mx_pos[ans] = i
    s += ans
    last = now

print('!', s, flush=True)
