def solve():
    cols = [[7], [4], [2, 8], [1, 5], [3, 9], [6], [10]]
    s = list(map(lambda x: bool(int(x)), list(input())))
    if s[0]:
        print("No")
        return
    col_states = []
    for col in cols:
        flag = False
        for c in col:
            flag |= s[c-1]
        col_states.append(flag)
    # print(col_states)

    for i in range(len(col_states)):
        for j in range(i):
            if col_states[i] and col_states[j]:
                for k in range(j+1, i):
                    if not col_states[k]:
                        print("Yes")
                        return

    print("No")
solve()
