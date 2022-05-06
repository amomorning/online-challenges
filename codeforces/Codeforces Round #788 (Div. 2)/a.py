cas = int(input())


for ca in range(cas):
    n = int(input())
    a = list(map(int, input().split())) 

    absA = list(map(abs, a))

    mni = 0
    mn = absA[0]
    for i in range(len(absA)):
        if(absA[i] < mn): 
            mn = absA[i]
            mni = i
    
    mxi = 0
    for i in range(len(absA)):
        if(absA[i] == mn):
            mxi = i
    
    
    flag = True
    for i in range(1, mni+1):
        if(absA[i] > absA[i-1]):
            flag = False
    for i in range(mni+1, len(absA)):
        if(absA[i] < absA[i-1]):
            flag = False
        
    cnt = 0
    for x in a:
        if(x < 0):
            cnt += 1
    
    if(cnt < mni or cnt > mxi+1):
        flag = False

    # print(cnt, mni, mxi)
    
    if(flag): print("YES")
    else: print("NO")

    

    
