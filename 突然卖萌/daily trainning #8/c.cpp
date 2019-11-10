#include <bits/stdc++.h>
const int N = 1e4+10;
typedef std::pair<int,int> P;

std::vector<P> G[N];
char a[N][22];
int mk[30];
int d[N], vis[N];

int get(int u, int v) {
	memset(mk, 0, sizeof(mk));
	int ret = 0;
	for(int i = 0; a[u][i]; ++ i) {
		if(a[u][i] < 'a') a[u][i] = a[u][i] - 'A'+'a';
		mk[a[u][i]-'a'] ++;
	}
	for(int i = 0; a[v][i]; ++ i) {
		if(a[v][i] < 'a') a[v][i] = a[v][i] - 'A'+'a';
		int t = a[v][i] - 'a';
		if(mk[t]) {
			ret ++;
			mk[t] = 0;
		}
	}	
	return ret;
}

void bfs(int s, int t) {
	memset(d, 0x3f, sizeof(d));
	std::priority_queue<P, std::vector<P>, std::greater<P> > pq;
	d[s] = 0;
	pq.push({d[s], s});
	while(!pq.empty()) {
		auto p = pq.top(); pq.pop();
		int u = p.second;
		if(p.first > d[u]) continue;
		for(auto e:G[u]) {
			if(d[e.first] > d[u] + e.second) {
				d[e.first] = d[u] + e.second;
				pq.push({d[e.first], e.first});
			}
		}	
	}
	printf("%d\n", d[t]);
}

int main() {
	int n; scanf("%d", &n);
	int m; scanf("%d", &m);
	for(int i = 0; i < n; ++ i) scanf("%s", a[i]);
	for(int i = 0; i < m; ++ i) {
		int u, v; scanf("%d%d", &u, &v);
		u --, v --;
		int w = get(u, v);
		G[u].push_back({v, w});
		G[v].push_back({u, w});
		// printf("%d\n", w);
	}
	int s, t; scanf("%d%d", &s, &t); 
	s --, t --;
	bfs(s, t);
}


