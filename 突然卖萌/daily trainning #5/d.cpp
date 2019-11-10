#include <bits/stdc++.h>
const int M = 1e4+10;

int dp[M][7];
int c[7][7] = {{},
	{2, 3, 4, 5},
	{1, 3, 4, 6},
	{1, 2, 5, 6},
	{1, 2, 5, 6},
	{1, 3, 4, 6},
	{2, 3, 4, 5}};

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d", &n);
		memset(dp, 0x3f, sizeof(dp));
		int ans = 0x3f3f3f3f;
		dp[0][1] = 0;
		for(int i = 0; i <= n; ++ i) {
			for(int k = 1; k <= 6; ++ k) {
				for(int j = 0; j < 4; ++ j) {
					int up = c[k][j];
					dp[i+up][up] = std::min(dp[i+up][up], dp[i][k] + 1);
				}
			}
		}
		for(int i = 1; i <= 6; ++ i) 
			ans = std::min(ans, dp[n][i]);
		if(ans == 0x3f3f3f3f) puts("-1"); 
		else printf("%d\n", ans);
	}
}
