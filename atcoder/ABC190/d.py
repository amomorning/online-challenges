import math
n = int(input())

cnt = 1
for i in range(3, int(math.sqrt(n*2))+1):
    if((2*n-i+i*i) % (2*i) == 0): cnt += 1

if(n%2 != 0 and n !=1): cnt += 1
print(cnt*2)
    


