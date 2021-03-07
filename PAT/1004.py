n, m = map(int, input().split())


def dfs(u, depth):
    global tree, count, md
    md = max(md, depth+1)
    if(len(tree[u]) == 0):
        count[depth] += 1
    for v in tree[u]:
        dfs(v, depth+1)


tree = {}
for i in range(n):
    tree[i] = []

for i in range(m):
    idx, k, *a = map(int, input().split())
    for u in a:
        tree[idx-1].append(u-1)

count = [0]*100
md = 0
dfs(0, 0)
print(" ".join(str(e) for e in count[:md]))
