import math
a, b, w = map(int, input().split())

mn = math.ceil(w*1000/b)
mx = math.floor(w*1000/a)

if(mx < mn): print('UNSATISFIABLE')
else: print(mn, mx)
