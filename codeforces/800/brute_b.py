
def check_a(s):
    while s.find('01') != -1:
        s = s.replace('01', '1')
    while s.find('10') != -1:
        s = s.replace('10', '0')
    return len(s) == 1

def check_b(s):
    while s.find('10') != -1:
        s = s.replace('10', '0')
    while s.find('01') != -1:
        s = s.replace('01', '1')
    return len(s) == 1

for _ in range(int(input())):
    n = int(input())
    s = input()

    tot = 0
    st = set()
    for i in range(n):
        for j in range(i, n):
            if check_a(s[i:j+1]) or check_b(s[i:j+1]):
                tot += 1
            else:
                st.add(s[i:j+1])
    st = sorted(st)
    for ss in st:
        print('s =', ss)
    print(tot)
