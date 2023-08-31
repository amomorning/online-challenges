#include <bits/stdc++.h>

int main() {
	int t;
	scanf("%d", &t);
	while (t --) {
		int n; scanf("%d", &n);
		int cur = 0;
		for(int i = 0; i < n; ++ i) {
			int l, r; scanf("%d%d", &l, &r);
			cur = std::max(cur, l);
			printf("%d ", cur > r? 0:cur++);
		}
	}
}
