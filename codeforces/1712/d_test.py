

def get_kth(k, arr, ref_idx):
    k = k - len(ref_idx) + 2

    for x, idx in ref_idx:
        if k < len(arr) and x <= arr[k][0]: k += 1
    
    assert k < len(arr)
    return arr[k]


a = [12, 1, 23, 12, 192, 11, 129, 233]

sort_a = sorted(list(zip(a, range(len(a)))))

idx = [0, 6]
ref_idx = sorted([(a[i], i) for i in idx])

print(sort_a)

print(get_kth(int(input()), sort_a, ref_idx))


