#include <bits/stdc++.h>
const int M = 110;

int dp[M][M][26];
int e[M][M];
int n, m;

int dfs(int u, int v, int c) {
	if(~dp[u][v][c]) return dp[u][v][c];
	int ret = 0;
	// printf("%d %d %d\n", u, v, c);
	for(int i = 0; i < n; ++ i) if(e[u][i] >= c) {
		if(dfs(v, i, e[u][i]) == 0) ret = 1;
	}
	return dp[u][v][c] = ret; 
}

int main() {
	scanf("%d%d", &n, &m);
	memset(dp, -1, sizeof(dp));
	memset(e, -1, sizeof(e));
	for(int i = 0; i < m; ++ i) {
		int u, v;
		char w[2];
		scanf("%d%d%s", &u, &v, w);
		u --, v --;
		e[u][v] = w[0]-'a';
	}
	dfs(0, 3, 0);
	for(int i = 0; i < n; i ++) {
		for(int j = 0; j < n; j ++) {
			if(dfs(i, j, 0)) printf("A");
			else printf("B");
		}	puts("");
	}
}	
