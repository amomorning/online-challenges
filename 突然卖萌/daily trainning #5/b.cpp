#include <bits/stdc++.h>
const int M = 1e5+10;

std::map<int, int> mp0, mp1, vis;
int a[M];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d", &n);
		for(int i = 0; i < n; ++ i) {
			int b; scanf("%d%d", &a[i], &b);
			mp0[a[i]] ++;
			mp1[b] ++;
			vis[a[i]] = 0;
		}
		long long ans = 0;
		for(int i = 0; i < n; ++ i) if(!vis[a[i]]) {
			ans += 1ll*mp0[a[i]] * mp1[a[i]];
			vis[a[i]] = 1;
		}
		printf("%lld\n", ans);
	}
}

