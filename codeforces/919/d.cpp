#include <bits/stdc++.h>
const int M	= 3e5+10;
char s[M];
int cnt[30];
int vis[M];
int dp[M][30];

std::vector<int> G[M];
bool flag;
int ans;

void dfs(int u) {
	if(vis[u] == 1) {
		flag = false;
		return;
	}
	if(vis[u] == 0) {
		for(int i = 0; i < 26; i ++) {

		}
	}
	vis[u] = 1;
	if(G[u].size() == 0) {
		for(int i = 0; i < 26; i ++) {
			ans = std::max(ans, dp[u][i]);
		}
	}
	for(size_t i = 0; i < G[u].size(); ++ i) {
		int v = G[u][i];
		for(int j = 0; j < 26; j ++) {
			dp[v][j] = dp[u][j];
		}
		dp[v][s[v] - 'a'] ++;
		dfs(v);
		if(!flag) return;
	}	
	vis[u] = 0;
}

int main() {
	int n, m;
	scanf("%d%d", &n, &m);
	scanf("%s", s);
	for(int i = 0; i < m; i ++) {
		int u, v;
		scanf("%d%d", &u, &v);
		u --, v --;
		G[u].push_back(v);
	}
	flag = true;
	ans = 0;
	memset(vis, -1, sizeof(vis));
	for(int i = 0; i < n; i ++) {
		if(vis[i] == -1) dfs(i);
	}
	if(flag) printf("%d\n", ans);
	else puts("-1");
}
