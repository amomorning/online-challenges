#include <stdio.h>
#include <string.h>
const int mod = 1e9+7;
const int M = 1010;

int dp[M][M];
inline void add(int &a, int b) {
	a += b;
	if(a >= mod) a -= mod;
}


int main() {
	int n, m;
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;
	for(int i = 0; i < M; i ++) {
		for(int j = 0; j <= i; j ++) {
			if(i) add(dp[i][j], dp[i-1][j]);
			if(j) add(dp[i][j], dp[i][j-1]);
		}
	}
	while(~scanf("%d%d", &n, &m)) {
		printf("%d\n", dp[n][m]);
	}
}
