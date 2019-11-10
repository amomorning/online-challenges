#include <bits/stdc++.h>
const int M = 110;

int a[2][M], dp[2][M];

int main() {
	int n; scanf("%d", &n);
	for(int i = 0; i < 2; i ++) 
		for(int j = 0; j < n; j ++) 
			scanf("%d", &a[i][j]);
	dp[0][0] = a[0][0];
	for(int i = 0; i < 2; i ++) {
		for(int j = 0; j < n; j ++) {
			if(i) dp[i][j] = std::max(dp[i][j], dp[i-1][j] + a[i][j]);
			if(j) dp[i][j] = std::max(dp[i][j], dp[i][j-1] + a[i][j]);
		}
	}
	printf("%d\n", dp[1][n-1]);
}
