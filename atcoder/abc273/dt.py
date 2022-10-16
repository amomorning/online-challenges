import bisect
a = [1, 2, 3, 4, 6, 9]

print(bisect.bisect_left(a, 1))
print(bisect.bisect_left(a, 5))
print(bisect.bisect_right(a, 5))

print(bisect.bisect_left(a, 10))

