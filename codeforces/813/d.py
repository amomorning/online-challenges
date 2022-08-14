import math

def get_kth(k, arr, ref):
    k = k - len(ref) + 2

    for x in ref:
        if k < len(arr) and x <= arr[k][0]: k += 1
    
    if k >= len(arr): return int(1e9)
    assert k < len(arr)
    return arr[k][0]

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k == n:
        print(int(1e9))
        continue
    
    sorted_a = sorted(list(zip(a, range(n))))
    # print(sorted_a)

    ans = 0
    for i in range(n-1):

        # 0, 0
        ref = sorted([a[j] for j in [i, i+1]])
        d = min(min(a[i], a[i+1]), get_kth(k, sorted_a, ref)*2)
        ans = max(d, ans)

        # 0, 1 
        d = min(a[i+1], get_kth(k-1, sorted_a, ref)*2)
        ans = max(ans, d)
        # 1, 0
        d = min(a[i], get_kth(k-1, sorted_a, ref)*2)
        ans = max(ans, d)

        if k == 1: continue
        
        d = min(int(1e9), get_kth(k-2, sorted_a, ref) * 2)
        ans = max(ans, d)
    print(ans)


        





