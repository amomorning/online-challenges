#include <bits/stdc++.h>
const int M = 1e3+10;
std::vector<int> G[M];
int f[M], id[M];

int main() {
	int n, m;
	scanf("%d%d", &n, &m);
	for(int i = 0; i < n; i ++) {
		scanf("%d", &f[i]);	
		id[i] = i;
	}
	std::sort(id, id+n, [](int x, int y) {
		return f[x] > f[y];
	});

	for(int j = 0; j < m; j ++) {
		int u, v; scanf("%d%d", &u, &v);
		u --, v --;
		G[u].push_back(v);
		G[v].push_back(u);
	}
	//for(int i = 0; i < n; i ++) printf("%d ", f[id[i]]);
	int ans = 0;
	for(int i = 0; i < n; i ++) {
		int d = id[i];
		for(auto x:G[d]) {
			ans += f[x];
		}
		f[d] = 0;
	}
	printf("%d\n", ans);
}
