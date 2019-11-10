#include <bits/stdc++.h>
using namespace std;
const int M = 1e5+10;
const int mod = 1e9+7;
const long long inf = 1e15;

struct edge{int v; long long w;};
std::vector<edge> G[M];
std::vector<int> pre[2][M];
typedef std::pair<long long, int> P;
long long d[2][M];

int n, m;
void dijkstra(int s, int x) {
	std::priority_queue<P, std::vector<P>, std::greater<P> > q;
	fill(d[x], d[x]+n, inf);
	d[x][s] = 0;
	q.push({0, s});
	while(!q.empty()) {
		P p = q.top(); q.pop();
		int u = p.second;
		if(d[x][u] < p.first) continue;
		for(int i = 0; i < (int)G[u].size(); i ++) {
			edge e = G[u][i];
			if(d[e.v] > d[u] + e.w) {
				pre[x][e.v].clear();
				d[x][e.v] = d[x][u] + e.w;
				q.push({d[x][e.v], e.w});
				pre[x][e.v].push_back(u);
			} else if(d[e.v] == d[u] + e.w) {
				pre[x][e.v].push_back(u);
			}	
		}
	}
}
int main() {
	int s, t;
	scanf("%d%d%d%d", &n, &m, &s, &t);
	for(int i = 0; i < m; i ++) {
		int u, v;
		long long d;
		scanf("%d%d%lld", &u, &v, &d);
		G[u].emplace_back(v, d);
		G[v].emplace_back(u, d);
	}
}
