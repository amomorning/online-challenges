n = int(input())
a = list(map(int, input().split()))

s = [0]*(n+1)
all_neg = True
for i in range(1, n+1):
    s[i] = s[i-1]+a[i-1]
    if(a[i-1] > 0):
        all_neg = False

# print(s)
l = 0
mx = 0
mxl, mxr = 0, 0
for r in range(1, n+1):
    if(s[r] < s[l]):
        l = r
    if(s[r]-s[l] > mx):
        mx = s[r]-s[l]
        mxl = l
        mxr = r

if(mxr == 0): mxr = n
for i in range(n):
    if(all_neg and a[i]==0): 
        mxl = i
        mxr = i+1

print("{} {} {}".format(mx, a[mxl], a[mxr-1]))




