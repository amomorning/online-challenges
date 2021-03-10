n, *a = map(int, input().split())

now = 0
tot = 0
for i in range(n):
    delta = a[i] - now
    now = a[i]
    if(delta > 0): 
        tot += delta * 6
    elif(delta < 0):
        tot += (-delta) * 4
    else: 
        tot += 0
        
print(tot + 5 * n)
    


