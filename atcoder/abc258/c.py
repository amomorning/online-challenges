n, q = map(int, input().split())
s = input()

cur = 0
for _ in range(q):
    op, x = map(int, input().split()) 
    if op == 1:
        cur -= x
    else:
        print(s[(x-1 + cur) % n])
