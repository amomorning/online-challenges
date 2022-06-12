#include <bits/stdc++.h>
int g[110][110];
int f[110][110][550];

int a, b, c, d;

bool check(int x) {
	int k = (c-a)*(d-b)/2;
	return f[c][d][x]-f[c][b][x]-f[a][d][x]+f[a][b][x] <= k;
}

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n, m, q; scanf("%d%d%d", &n, &m, &q);
		for(int i = 1; i <= n; ++ i) {
			for(int j = 1; j <= m; ++ j) {
				scanf("%d", &g[i][j]);
			}
		}
		for(int i = 1; i <= n; ++ i) {
			for(int j = 1; j <= m; ++ j) {
				for(int x = 1; x <= 500; ++ x) {
					f[i][j][x] = f[i-1][j][x]+f[i][j-1][x]-f[i-1][j-1][x]+(g[i][j]>x);
				}
			}
		}
		
		for(int i = 0; i < q; ++ i) {
			scanf("%d%d%d%d", &a, &b, &c, &d);
			a --, b --;
			int l = 0, r = 500;
			while(l+1 < r) {
				int mid = (l+r) >> 1;
				if(check(mid)) r = mid;
				else l = mid;
			}
			printf("%d\n", r);
		}
	}
}
