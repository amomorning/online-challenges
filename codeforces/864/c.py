def answer(a, b):
    print(f'! {a} {b}', flush=True)

def ask(a, b):
    print(f'? {a} {b}', flush=True)
    return int(input())
    
def solve():
    n, m = map(int, input().split())
    a = ask(1, 1)
    b = ask(n, m)
    if a + b == n - 1:
        x = 1 + a
        y = 1 + ask(x, 1)
    elif a + b == m - 1:
        y = 1 + a
        x = 1 + ask(1, y)
    else:
        if 1 + a <= n and m - b >= 1 and ask(1 + a, m - b) == 0:
            x = 1 + a
            y = m - b
        else:
            x = n - b
            y = 1 + a 
    answer(x, y)


for _ in range(int(input())):
    solve()



