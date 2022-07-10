import bisect
a = [1, 1, 1, 2, 2, 2, 3, 3, 6, 6, 8, 8, 8, 9]

def get_range(x):
    l = bisect.bisect_left(a, x)
    r = bisect.bisect_right(a, x)
    return l, r, a[l], a[r-1]

print(len(a))
print(get_range(0))
print(get_range(1))
print(get_range(2))
print(get_range(5))
print(get_range(6))
print(get_range(9))

del a[0]
print(a)

