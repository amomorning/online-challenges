#include <bits/stdc++.h>

int main() {
	int n, m; scanf("%d%d", &n, &m);
	double ans = 1e15;
	for(int i = 0; i < n; i ++) {
		int a, b; scanf("%d%d", &a, &b);
		ans = std::min(ans, 1.0*m*a/b);
	}
	printf("%.8f\n", ans);
}
