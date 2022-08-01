n = int(input())

a = list(map(lambda x: int(x)-1, input().split()))

equals = 0
swaps = 0
for i in range(n):
    if i == a[i]:
        equals += 1
    elif a[a[i]] == i:
        swaps += 1

print(swaps//2 + equals * (equals - 1) // 2)
