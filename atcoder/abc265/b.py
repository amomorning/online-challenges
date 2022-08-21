n, m, t = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * n
for i in range(m):
    x, y = map(int, input().split())
    b[x-1] += y

flag = True
for i in range(n-1):
    t += b[i]
    if t <= a[i]:
        flag = False
        break
    else:
        t -= a[i]
    # print(t)
print("Yes") if flag else print("No")
