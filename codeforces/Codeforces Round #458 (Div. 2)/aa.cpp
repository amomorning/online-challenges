#include <bits/stdc++.h>

int main() {
	int n;
	scanf("%d", &n);
	int ans = -1e6-7;
	for(int i = 0; i < n; i ++) {
		int x;
		scanf("%d", &x);
		if(x < 0) {
			ans = std::max(ans, x);
			continue;
		}
		int t = pow(x, 0.5);
		if(t*t!=x) ans = std::max(ans, x);
	}
	printf("%d\n", ans);
}
