#include <bits/stdc++.h>
using namespace std;
const int M = 2e5+10;

queue<int> a[M];
int x[M], d[M];

void bfs(int n) {
	memset(d, 0x3f, sizeof(d));
	d[0] = 0;
	priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > q;
	q.push({d[0], 0});
	while(!q.empty()) {
		if(d[n-1] != 0x3f3f3f3f) break;
		pair<int, int> p = q.top(); q.pop();
		int c = x[p.second];
		while(!a[c].empty()) {
			int id = a[c].front(); a[c].pop();
			if(id == p.second || d[id] < d[p.second]+1) continue;
			d[id] = d[p.second] + 1;
			q.push({d[id], id});
			break;
		}
		if(d[p.second+1] > d[p.second]+1) {
			d[p.second+1] = d[p.second] + 1;
			q.push({d[p.second+1], p.second+1});
		}
	}
	printf("%d\n", d[n-1]);
}

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d", &n);
		for(int i = 0; i < M; ++ i) while(!a[i].empty()) a[i].pop();
		for(int i = 0; i < n; ++ i) {
			scanf("%d", &x[i]);
			a[x[i]].push(i);
		}
		bfs(n);
	}
}
