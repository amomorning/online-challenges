#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> P;
vector<P> G[20];

int vis[20], mn[20];

void dfs(int u, int mask) {
	if(vis[u]) return;
	vis[u] = 1;
	for(auto e:G[u]) if(mask&(1<<e.first)) {
		dfs(e.first, mask);
	}
	return;
}

bool judge(int mask) {
	int cnt = 0;
	memset(vis, 0, sizeof(vis));
	for(int i = 0; i < 20; ++ i) if((mask|(1<<i)) && !vis[i]) {
		dfs(i, mask);
		cnt ++;
	}
	return cnt == 1;
}

int prim(int mask) {
	int ret = 0;
	priority_queue<P, vector<P>, greater<P> > pq;
	memset(vis, 0, sizeof(vis));
	memset(mn, 0, sizeof(mn));
	int s = __builtin_ffs(mask)-1;	
	mn[s] = 0;
	pq.push({mn[s], s
	return ret;
}

int main() {
	int t; scanf("%d", &t);
	while( t --) {
		for(int i = 0; i < 15; ++ i) G[i].clear();
		int n, m, k; scanf("%d%d%d", &n, &m, &k);
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
			if(judge(i)) {
				ans = min(ans, prim(i));
			}
		}
	}
}
