import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))

def solve(cas):
    s = input()
    ans = 'A' if s.count('A') > s.count('B') else 'B'
    print(ans)

cas = 1
cas = int(input())
for _ in range(cas):
    solve(_)


