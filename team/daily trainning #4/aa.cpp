#include <bits/stdc++.h>
const int N = 1e5+10;

int a[N];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d", &n);
		for(int i = 0; i < n; ++ i) {
			scanf("%d", &a[i]);
		}
		long long ans = 0;
		for(int j = 0; j < 21; ++ j) {
			for(int i = 0; i < n; ++ i) {
				int cnt = 0;
				while((a[i]&(1<<j)) && i < n) {
					++ cnt;
					++ i;
				}
				if(cnt) -- i;
				ans += 1ll*(cnt+1)*cnt/2*(1<<j);
			}
		}
		printf("%lld\n", ans);
	}
}
