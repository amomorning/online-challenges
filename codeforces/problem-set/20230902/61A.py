import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")

a = input()
b = input()
t = []
for i in range(len(a)):
    if a[i]!=b[i]:
        t.append('1')
    else:
        t.append('0')
print(''.join(t))
