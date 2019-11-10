#include <bits/stdc++.h>
const int N = 2e3+10;

struct edge{
	int v, c, d;
};
std::vector<edge> G[N];

int s, t;
std::vector<int> id;
std::vector<std::pair<int, int> > ans;
int vis[N], mk[N];

void dfs(int u) {
	vis[u] = 1;
	if(u == t) {
		int l = 0, r = 0x3f3f3f3f;
		for(size_t i = 1; i <= id.size(); ++ i) {
			if(mk[i] > 0) l = std::max(l, (int)i);
			if(mk[i] < 0) r = std::min(r, (int)i);
		}
		if(l <= r) ans.push_back({l, r});
	}
	for(auto e:G[u]) {
		int pl = std::lower_bound(id.begin(), id.end(), e.c)-id.begin();
		int pr = std::lower_bound(id.begin(), id.end(), e.d)-id.begin();
		mk[pl] ++;
		mk[pr] --;
		if(!vis[e.v]) dfs(e.v);
		mk[pl] --;
		mk[pr] ++;
	}
	vis[u] = 0;
}

int main() {
	int n, m, k;
	scanf("%d%d%d%d%d", &n, &m, &k, &s, &t);
	
	for(int i = 0; i < m; ++ i) {
		int a, b, c, d; 
		scanf("%d%d%d%d", &a, &b, &c, &d);
		id.push_back(c);
		id.push_back(d);	
		G[a].push_back({b,c,d});
		G[b].push_back({a,c,d});
	}
	std::sort(id.begin(), id.end());
	auto x = std::unique(id.begin(), id.end());
	id.erase(x, id.end());
	dfs(s);
	int l = ans[0].first, r = ans[0].second;
	int ret = 0;
	for(int i = 1; i < (int)ans.size(); ++ i) {
		if(ans[i].first > r) {
			ret += r-l+1;
			l = ans[i].first;
			r = ans[i].second;
		} else {
			r = std::max(r, ans[i].second);
		}
	}
	ret += r-l+1;
	printf("%d\n", ret);
}
