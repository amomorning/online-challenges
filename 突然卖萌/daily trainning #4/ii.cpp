#include <bits/stdc++.h>
using namespace std;
const int N = 2e5+10;

int a[N], ls[N], d[N];
vector<int> G[N];

void bfs(int n) {
	queue<int> q;
	q.push(0);
	memset(d, 0x3f, sizeof(d));
	d[0] = 0;
	bool flag = false;
	while(!q.empty()) {
		int u = q.front(); q.pop();
		for(auto v:G[u]) {
			d[v] = min(d[v], d[u]+1);
			q.push(v);
			if(v == n-1) {
				flag = true;
			}
		}
		if(flag) break;
	}
	printf("%d\n", d[n-1]);
}

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d", &n);
		memset(ls, -1, sizeof(ls));
		for(int i = 0; i < n-1; ++ i) {
			G[i].push_back(i+1);
		}
		for(int i = 0; i < n; ++ i) {
			scanf("%d", &a[i]);
			if(ls[a[i]] != -1) G[ls[a[i]]].push_back(i);
			ls[a[i]] = i;
		}
		bfs(n);
	}
}
