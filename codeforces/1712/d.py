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

    ans = 0
    for i in range(n-1):
        ref = sorted([a[j] for j in [i, i+1]])
        for p in range(2):
            for q in range(2):
                if k-p-q < 0: continue
                x = int(1e9) if p else a[i]
                y = int(1e9) if q else a[i+1]
                d = min(min(x, y), get_kth(k-p-q, sorted_a, ref)*2)
                ans = max(ans, d)
    print(ans)


        





