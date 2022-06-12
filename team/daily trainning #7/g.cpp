#include <bits/stdc++.h>
const int N = 1e3+10;

struct edge {
	int v, c, d;
};

std::vector<edge> G[N];
int vis[N];
std::vector<std::pair<int, int> > to;
std::vector<std::pair<int, int> > ans;
int s, t;

void dfs(int u) {
	vis[u] = 1;
	if(u == t) {
		int l = to[0].first, r = to[0].second;
		for(auto p:to) {
			// printf("%d %d\n", p.first, p.second);
			l = std::max(l, p.first);
			r = std::min(r, p.second);
		}
		// puts("--");
		if(l <= r) ans.push_back({l, r});
	}
	for(auto e:G[u]) {
		to.push_back({e.c, e.d});
		if(!vis[e.v]) dfs(e.v);
		to.erase(to.end());
	}
	vis[u] = 0;
}

int main() {
	int n, m, k;
	scanf("%d%d%d%d%d", &n, &m, &k, &s, &t);
	for(int i = 0; i < m; ++ i) {
		int a, b, c, d; 
		scanf("%d%d%d%d", &a, &b, &c, &d);
		G[a].push_back({b,c,d});
		G[b].push_back({a,c,d});
	}
	dfs(s);
	std::sort(ans.begin(), ans.end());
	int ret = 0;
	int l = ans[0].first, r = ans[0].second;
	for(size_t i = 1; i < ans.size(); ++ i) {
		if(ans[i].first > r) {
			ret += r-l+1;;
			l = ans[i].first;
			r = ans[i].second;
		} else {
			r = std::max(r, ans[i].second);
		}
	}
	ret += r-l+1;
	printf("%d\n", ret);
}
