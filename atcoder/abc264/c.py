


def count_one(num):
    cnt = 0
    for i in range(num.bit_length()):
        if num & (1<<i):
            cnt += 1
    return cnt

def get_idx(num):
    ret = []
    for i in range(num.bit_length()):
        if num & (1<<i):
            ret.append(i)
    return ret
def solve():
    h1, w1 = map(int, input().split())
    A = []
    for i in range(h1):
        A.append(list(map(int, input().split())))

    h2, w2 = map(int, input().split())
    B = []
    for i in range(h2):
        B.append(list(map(int, input().split())))
    for h in range(1<<h1):
        if count_one(h) == h2:
            for w in range(1<<w1):
                if count_one(w) == w2:
                    flag = True
                    for i in range(h2):
                        for j in range(w2):
                            id_i = get_idx(h)
                            id_j = get_idx(w)
                            if A[id_i[i]][id_j[j]] != B[i][j]:
                                flag = False
                    if flag:
                        print("Yes")
                        return
    print("No")
    return

solve()


