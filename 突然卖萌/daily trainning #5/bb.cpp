#include <bits/stdc++.h>
const int M = 1e5+10;
int a[M], b[M];
std::map<int, int> mp;
int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d", &n);
		mp.clear();
		for(int i = 0; i < n; ++ i) {
			scanf("%d%d", &a[i], &b[i]);
			mp[a[i]] ++;
		}
		long long ans = 0;
		for(int i = 0; i < n; ++ i) {
			ans += mp[b[i]];
		}
		printf("%lld\n", ans);
	}
}
