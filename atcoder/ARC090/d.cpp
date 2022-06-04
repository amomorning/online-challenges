#include <bits/stdc++.h>
const int M = 2e5+10;

int f[M];
int d[M];

int find(int x) {
	if(f[x] == -1) return x;
	int fa = f[x];
	f[x] = find(fa);
	d[x] += d[fa];
	return f[x];
}

int main() {
	int n, m;
	scanf("%d%d", &n, &m);
	memset(f, -1, sizeof(f));
	bool flag = true;
	for(int i = 0; i < m; i ++) {
		int u, v, w;
		scanf("%d%d%d", &u, &v, &w);
		u --, v --;
		int fa = find(u);
		int fb = find(v);
		// printf("%d %d\n", fa, fb);
		if(fa == fb) {
			if(d[v]-d[u] != w) flag = false;
		} else {
			f[fb] = fa;
			d[fb] = d[u] - d[v] + w;
		}
	}
	if(flag) puts("Yes");
	else puts("No");
}
