#include <bits/stdc++.h>
const int M = 1e5+10;
std::vector<int> G[M];
int co[M];

void dfs(int u, int p, int c) {
	co[u] = c;
	for(auto v:G[u]) {
		if(v == p) continue;
		dfs(v, u, !c);
	}
}

int main() {
	int n; scanf("%d", &n);
	for(int i = 1; i < n; ++ i) {
		int u, v; scanf("%d%d", &u, &v);
		G[u].push_back(v);
		G[v].push_back(u);
	}
	dfs(1, -1, 0);
	int cnt = 0;
	for(int i = 1; i <= n; ++ i) {
		if(co[i]) cnt ++;
	}
	printf("%lld\n", 1ll*cnt*(n-cnt)-n+1);
}
