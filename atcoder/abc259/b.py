
import math

a, b, d= map(int, input().split())

p, ro = math.sqrt(a**2 + b**2), math.atan2(b, a)

ro += d/180*math.pi
if ro > math.pi * 2:
    ro -= math.pi * 2

print(p * math.cos(ro), p * math.sin(ro))

