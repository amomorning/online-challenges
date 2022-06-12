n, H = map(int, input().strip().split());

def c(x):
    if(x>H): tmp = (H+x)*(x-H+1)/2+x*(x-1)/2
    else: tmp = (1+x)*x/2
    if(tmp <= n): return True
    else: return False

l, r = 0, n
while(l <= r):
    mid = int((l+r)/2)
    #  print(mid)
    if(c(mid)):
        ans = mid 
        l = mid+1
    else:
        r = mid-1

#  print(ans)
if(ans > H): 
    tmp = n*2 - (((H+ans)*(ans-H+1))+ans*(ans-1))
    tmp = int(tmp/2)
    if(tmp > ans): print(ans*2-H+2)
    elif(tmp > 0): print(ans*2-H+1)
    else: print(ans*2-H)
else: 
    tmp = n*2-((1+ans)*ans)
    tmp = int(tmp/2)
    #  print(tmp)
    if(tmp > ans): print(ans+2)
    elif(tmp > 0): print(ans+1)
    else: print(ans)
