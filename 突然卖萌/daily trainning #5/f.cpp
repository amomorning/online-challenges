#include <bits/stdc++.h>
const int M = 1e5+10;

int a[M];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n, q; scanf("%d%d", &n, &q);
		for(int i = 1; i <= n; ++ i) {
			long long x; scanf("%lld", &x);
			int cnt = 0;
			while(x > 1) {
				if(x&1) cnt ++;
				x/=2;
				cnt ++;
			}
			// printf("%d ", cnt);
			a[i] = a[i-1] + cnt;
		}
		// puts("");
		while(q --) {
			int l, r;
			scanf("%d%d", &l, &r); l --;
			printf("%d\n", a[r]-a[l]);
		}
	}
}
