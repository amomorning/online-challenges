#include <bits/stdc++.h>
const int M = 1e5+10;
int x[M], y[M];

int main() {
	int n; scanf("%d", &n);
	for(int i = 0; i < n; ++ i) {
		scanf("%d", &x[i]);
	}
	int res = 0x3f3f3f3f;
	for(int a = -1; a < 2;  ++ a) {
		for(int b = -1; b < 2; ++ b) {
			int d = x[1]+b-(x[0]+a);
			int f = 0;
			int ans = abs(b) + abs(a);
			y[1] = x[1]+b;
			y[0] = x[0]+a;
			for(int i = 2; i < n; ++ i) {
				y[i] = x[i];
			}
			for(int i = 2; i < n; ++ i) {
				f = y[i]-y[i-1]-d;
				// printf("%d %d\n", d, f);
				if(abs(f) > 1) break;
				y[i] -= f;
				ans += abs(f);
			}
			if(abs(f) <= 1) res = std::min(res, ans);
		}
	}
	if(res == 0x3f3f3f3f) puts("-1");
	else printf("%d\n", res);
}
