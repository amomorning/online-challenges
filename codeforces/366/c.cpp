#include <bits/stdc++.h>
const int M = 1e5;
int a[110], b[110];
int dp[M<<1]; 

int main() {
	int n, k; scanf("%d%d", &n, &k);
	for(int i = 0; i < n; ++ i) scanf("%d", &a[i]);
	for(int i = 0; i < n; ++ i) {scanf("%d", &b[i]); b[i] = a[i]-b[i]*k;}
	memset(dp, -1, sizeof(dp));
	dp[M] = 0;
	for(int i = 0; i < n; ++ i) {
		if(b[i] >= 0) {
			for(int j = (M<<1)-b[i]; j >= 0; -- j) if(~dp[j])
				dp[j+b[i]] = std::max(dp[j+b[i]], dp[j]+a[i]);
		} else {
			for(int j = -b[i]; j <= (M<<1); ++ j) if(~dp[j]) 
				dp[j+b[i]] = std::max(dp[j+b[i]], dp[j]+a[i]);
		}
	}
	printf("%d\n", dp[M]?dp[M]:-1);
}
