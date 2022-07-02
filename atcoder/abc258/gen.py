from bisect import bisect_left

a = list(range(0, 5)) + list(range(6, 10))

b = bisect_left(a, 100)
print(b)
