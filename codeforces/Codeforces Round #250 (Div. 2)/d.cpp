#include <bits/stdc++.h>
const int M = 1e5+10;

int f[M], u[M], v[M], w[M], a[M], id[M], num[M];

int find(int x) {
	if(f[x] == -1) return x;
	return f[x] = find(f[x]);
}

int main() {
	int n, m;
	scanf("%d%d", &n, &m);
	memset(f, -1, sizeof(f));
	for(int i = 0; i < n; i ++) {
		scanf("%d", &a[i]);
		num[i] = 1;
	}
	for(int i = 0; i < m; i ++) {
		scanf("%d%d", &u[i], &v[i]);
		u[i] --, v[i] --;
		w[i] = std::min(a[u[i]], a[v[i]]);
		id[i] = i;
	}
	std::sort(id, id+m, [](int x, int y) {
		return w[x] > w[y];
	});
	long long sum = 0;
	for(int x = 0; x < m; x ++) {
		int i = id[x];
		int fa = find(u[i]);
		int fb = find(v[i]);
		if(fa == fb) continue;
		sum += 1ll*w[i]*num[fa]*num[fb]*2;
		f[fb] = fa;
		num[fa] += num[fb];
	}
	printf("%f\n",1.0*sum/n/(n-1));
}
