def get_str(s):
    cnt = 1
    cur = s[0]
    ret = []
    for i, j in zip(s, s[1:]):
        if i == j:
            cnt += 1
        else:
            ret.append((cur, cnt))
            cnt = 1
            cur = j
    ret.append((cur, cnt))
    return ret

def solve():

    s = input()
    t = input()

    ls = get_str(s)
    lt = get_str(t)

    if len(lt) != len(ls):
        print("No")
        return

    for a, b in zip(ls, lt):
        if a[0] != b[0]:
            print("No")
            return
        if b[1] != a[1] and a[1] == 1:
            print("No")
            return
        if b[1] < a[1]:
            print("No")
            return
    print("Yes")    


solve()
