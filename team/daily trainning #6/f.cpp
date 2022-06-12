#include <bits/stdc++.h>

int g[110][110];
int f[110][110][550];
int a, b, c, d;

bool judge(int x) {
	int ret = 0;
	for(int i = a; i <= c; ++ i) {
		ret += f[i][d][x] - f[i][b][x];
	}
	return ret <= (c-a+1)*(d-b+1)/2;
}


int main() {
	int t; scanf("%d", &t);
	while(t --) {
		memset(f, 0, sizeof(f));
		int n, m, q;
		scanf("%d%d%d", &n, &m, &q);
		for(int i = 1; i <= n; ++ i) {
			for(int j = 1; j <= m; ++ j) {
				scanf("%d", &g[i][j]);
				for(int k = 0; k < g[i][j]; ++ k) {
					f[i][j][k] ++;
					f[i][j][k] += f[i][j-1][k]; 
				}
			}
		}
		for(int i = 0; i < q; ++ i) {
			scanf("%d%d%d%d", &a, &b, &c, &d);
			int l = 0, r = 500;
			while(l < r) {
				int mid = (l+r) >> 1;
				if(judge(mid)) {
					r = mid;
				} else l = mid+1;
			}
			printf("%d\n", r);
		}
	}
}
