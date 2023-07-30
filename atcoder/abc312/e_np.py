import sys
import numpy as np

def solve(X):
    N = X.shape[0]
    M = 101
    A = np.full((M, M, M), -1, np.int64)
    ans = np.zeros(N, np.int64)

    def all_faces(x0, y0, z0, x1, y1, z1):
        return [
            A[x0:x1, y0:y1, z0],
            A[x0:x1, y0:y1, z1-1],
            A[x0:x1, y0, z0:z1],
            A[x0:x1, y1-1, z0:z1],
            A[x0, y0:y1, z0:z1],
            A[x1-1, y0:y1, z0:z1],
        ]
    
    def all_outer_faces(x0, y0, z0, x1, y1, z1):
        return [
            A[x0:x1, y0:y1, z0-1],
            A[x0:x1, y0:y1, z1],
            A[x0:x1, y0-1, z0:z1],
            A[x0:x1, y1, z0:z1],
            A[x0-1, y0:y1, z0:z1],
            A[x1, y0:y1, z0:z1]
        ]

    for i in range(N):
        x0, y0, z0, x1, y1, z1 = X[i]
        for f in all_faces(x0, y0, z0, x1, y1, z1):
            f[:] = i

        s = set()
        for f in all_outer_faces(x0, y0, z0, x1, y1, z1):
            for b in f.ravel():
                if b != -1: s.add(b)
            
        for j in s:
            ans[i] += 1
            ans[j] += 1

    return ans


def main():
    N = int(input())
    X = np.fromstring(sys.stdin.read(), np.int64, sep=' ').reshape(-1, 6)
    print('\n'.join(map(str, solve(X).tolist())))

if __name__ == '__main__':
    if sys.argv[-1] == 'ONLINE_JUDGE':
        from numba.pycc import CC
        cc = CC('my_module')
        cc.export('solve', 'i8[:](i8[:,:])')(solve)
        cc.compile()
        exit()
    from my_module import solve
    main()
