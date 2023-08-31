#include <bits/stdc++.h>
const int M = 2e5+10;

std::list<int> ls;
std::vector<int> G[M];
int f[M], cnt[M], no[M], vis[M];

int find(int x) {
	return x == f[x] ? x:f[x] = find(f[x]);
}

int main() {
	int n, m; scanf("%d%d", &n, &m);
	for(int i = 0; i < n; ++ i) {
		ls.push_back(i);
		f[i] = i;
	}	
	for(int i = 0; i < m; ++ i) {
		int u, v;
		scanf("%d%d", &u, &v);
		--u , -- v;
		G[u].push_back(v);
		G[v].push_back(u);
	}
	std::queue<int> q;
	for(int i = 0; i < n; i ++) {
		if(!vis[i]) q.push(i);
		while(!q.empty()) {
			int u = q.front(); q.pop(); vis[u] = 1;
			int fa = find(u);
			for(auto v:G[u]) no[v] = 1;
			for(auto it = ls.begin(); it != ls.end(); ) {
				if(!no[*it] && fa != find(*it)) {
					f[*it] = fa;
					q.push(*it);
					ls.erase(it ++);
				} else it ++;
			}
			for(auto v:G[u]) no[v] = 0;
		}
	}
	for(int i = 0; i < n; i ++) {
		int fa = find(i);
		cnt[fa] ++;
	}
	std::sort(cnt, cnt +n);
	int id = 0;
	while(cnt[id] == 0) id ++;
	printf("%d\n", n-id);
	for(int i = id; i < n; ++ i) printf("%d ", cnt[i]);
}
