f = [1] * 11

for i in range(1, 11):
    f[i] = f[i-1] * i

n = int(input())
print(f[n])
