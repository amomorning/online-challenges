#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> P;
vector<P> G[20];


int mn[20], vis[20];
int prim(int mask) {
	int res = 0;
	std::priority_queue<P, vector<P>, greater<P> > pq;
	memset(mn, 0x3f, sizeof(mn));
	memset(vis, 0, sizeof(vis));
	int s = __builtin_ffs(mask)-1;
	mn[s] = 0;
	pq.push({mn[s], s});
	// printf("s == %d %d\n", s, mask);
	while(!pq.empty()) {
		P p = pq.top(); pq.pop();
		int u = p.second;
		if(vis[u] == 1) continue;
		vis[u] = 1;
		res += p.first;
		for(auto e:G[u]) if(mask&(1<<e.first)) {
			if(mn[e.first] > e.second) {
				mn[e.first] = e.second;
				pq.push({mn[e.first], e.first});
			}
		}
	}
	for(int i = 0; i < 20; ++ i) if(mask&(1<<i)) {
		if(vis[i] == 0) return 0x3f3f3f3f;
	}
	return res;
}

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n, m, k; scanf("%d%d%d", &n, &m, &k); 
		for(int i = 0; i < 20; ++ i) G[i].clear();
		for(int i = 0; i < m; ++ i) {
			int u, v, c; scanf("%d%d%d", &u, &v, &c);
			u --, v --;
			G[u].emplace_back(v, c);
			G[v].emplace_back(u, c);
		}
		int init = 0;
		for(int i = 0; i < k; ++ i) {
			int x; scanf("%d", &x);
			init |= (1<<(x-1));
		}
		int ans = 0x3f3f3f3f;
		for(int i = init; i < (1<<n); i = (i+1)|init) {
			ans = min(ans, prim(i));
		}
		printf("%d\n", ans);
	}
}
