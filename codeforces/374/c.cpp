#include <bits/stdc++.h>
const int inf = 0x3f3f3f3f;
const int M = 1e3+10;

char mp[M][M];
int f[M][M];
bool vis[M][M];
int n, m;

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

int dfs(int x, int y) {
	if(vis[x][y]) return inf;
	if(~f[x][y]) return f[x][y];
	vis[x][y] = 1;
	int ret = 0;
	for(int i = 0; i < 4; ++ i) {
		int ex = x + dx[i]; 
		int ey = y + dy[i];
		if(ex < 0 || ey < 0 || ex >= n || ey >= m) continue;
		if(mp[x][y] == 'D' && mp[ex][ey] == 'I') ret = std::max(ret, dfs(ex, ey));
		if(mp[x][y] == 'I' && mp[ex][ey] == 'M') ret = std::max(ret, dfs(ex, ey));
		if(mp[x][y] == 'M' && mp[ex][ey] == 'A') ret = std::max(ret, dfs(ex, ey));
		if(mp[x][y] == 'A' && mp[ex][ey] == 'D') ret = std::max(ret, dfs(ex, ey));
	}
	vis[x][y] = 0;
	return f[x][y] = mp[x][y] == 'A'? ret+1:ret;
}

int main() {
	scanf("%d%d", &n, &m);
	memset(f, -1, sizeof(f));
	for(int i = 0; i < n; ++ i) scanf("%s", mp[i]);
	for(int i = 0; i < n; ++ i) {
		for(int j = 0; j < m; ++ j) if(mp[i][j] == 'D') {
			dfs(i, j);
		}
	}
	int ans = 0;
	for(int i = 0; i < n; ++ i) {
		for(int j = 0; j < m; ++ j) {
			ans = std::max(ans, f[i][j]);
		}
	}
	if(ans >= inf) printf("Poor Inna!");
	else if(ans) printf("%d\n", ans);
	else puts("Poor Dima!");
}
