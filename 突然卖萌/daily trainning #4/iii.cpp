#include <bits/stdc++.h>
using namespace std;
const int N = 2e5+10;

int a[N], ls[N], dp[N];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d", &n);
		memset(dp, 0x3f, sizeof(dp));
		memset(ls, -1, sizeof(ls));
		for(int i = 0; i < n; ++ i) {
			scanf("%d", &a[i]);
		}
		dp[0] = 0;
		ls[a[0]] = 0;
		for(int i = 1; i < n; ++ i) {
			dp[i] = min(dp[i], dp[i-1] + 1);
			if(~ls[a[i]]) dp[i] = min(dp[i], dp[ls[a[i]]]+1);
			ls[a[i]] = i;
		}
		printf("%d\n", dp[n-1]);
	}
}
