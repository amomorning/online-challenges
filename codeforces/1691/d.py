import sys; input = lambda:sys.stdin.readline().strip("\r\n")
import platform; LOCAL = (platform.uname().node == 'AMO')

def printf(a):
    if LOCAL:
        print('>>>:', end=' ')
    
    if(isinstance(a, list)):
        print(' '.join(map(str, a)))
    else:
        print(a)


class SparseTable:
    def __init__(self, a, select=min):
        n = len(a); L = 1
        while (1 << L) <= n: L += 1

        self.lg = [-1] * (n + 1)
        self.u = [[0] * (L+1) for _ in range(n)]
        self.select = select

        for i in range(n):
            self.u[i][0] = a[i]
        for i in range(1, n + 1):
            self.lg[i] = self.lg[i >> 1] + 1
        for j in range(1, L):
            for i in range(n-(1<<j)+1):
                self.u[i][j] = self.select(self.u[i][j - 1], self.u[i + (1 << (j - 1))][j - 1])
        
    def ask(self, a, b):
        k = self.lg[b-a+1]
        return self.select(self.u[a][k], self.u[b - (1 << k) + 1][k])



for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    prefix = [a[0]]
    for i in range(1, n):
        prefix.append(a[i] + prefix[-1])
    suffix = [a[n-1]]
    for i in range(n-2, -1, -1):
        suffix.append(a[i] + suffix[-1])
    suffix.reverse()
    stp = SparseTable(prefix, max)
    sts = SparseTable(suffix, max)
    left = [-1] * n
    right = [-1] * n

    for i in range(n):
        left[i] = i
        while left[i] > 0 and a[left[i]-1] <= a[i]:
            left[i] = left[left[i]-1]
    
    for i in range(n-1, -1, -1):
        right[i] = i
        while right[i] < n-1 and a[right[i] + 1] <= a[i]:
            right[i] = right[right[i]+1]

    flag = True
    for i in range(n):
        l, r = 0, 0
        if left[i] < i:
            l = sts.ask(left[i], i) - suffix[i]
        if right[i] > i:
            r = stp.ask(i, right[i]) - prefix[i]

        if l + r > 0:
            flag = False


    printf("YES") if flag else printf("NO")
