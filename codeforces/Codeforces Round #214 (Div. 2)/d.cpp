#include <bits/stdc++.h>
const int M = 1e3+10;

int u[M], v[M], l[M], r[M];
int f[M];

int find(int x) {
	return f[x] == x ? x : f[x] = find(f[x]);
}

int main() {
	int n, m; scanf("%d%d", &n, &m);
	for(int i = 1; i <= n; ++ i) f[i] = i;
	for(int i = 0; i < m; ++ i) {
		scanf("%d%d%d%d", &u[i], &v[i], &l[i], &r[i]);
	}
	int len = 0, R, L;
	for(int i = 0; i < n; ++ i) {
		if(u[i] == 1) {
			if(r[i] - l[i] > len) {
				R = r[i];
				L = l[i];
			}
		} 
		if(v[i] == 1) {
			if(r[i] - l[i] > len) {
				R = r[i];
				L = l[i];
			}
		} 
	}
	
	while(find(n) != 1) {
		int nlen = 0, up = -1, nl, nr;
		for(int i = 0; i < n; ++ i) {
			int fu = find(u[i]);
			int fv = find(v[i]);
			if(fu == fv) continue;
			int llen = r[i] - l[i];
			if(fu == 1) {
				if(l[i] < L && R < r[i]) {
					f[fv] = fu;
					continue;
				}
				if(l[i] < L) llen = r[i] - L;
				if(r[i] > R) llen = R - l[i];
			}
			else if(fv == 1) {
				if(l[i] < L && R < r[i]) {
					f[fv] = fu;
					continue;
				}
				if(l[i] < L) llen = r[i] - L;
				if(r[i] > R) llen = R - l[i];
			} else continue;
			if(llen > nlen) {
				up = std::max(fv, fu);
				nl = l[i], nr = r[i];
			}
		}
		f[up] = 1;
		if(up == -1) return puts("Nice work, Dima!"), 0;
		R = std::min(R, nr);
		L = std::max(L, nl);
	}
	printf("%d %d\n", L, R);
	printf("%d\n", R-L+1);
}

