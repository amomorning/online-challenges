#include <bits/stdc++.h>
const int M = 220;

int a[M];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n, m; scanf("%d%d", &n, &m);
		for(int i = 0; i < m; ++ i) {
			scanf("%d", &a[i]);
		}
		int ans = a[0];
		for(int i = 1; i < m; ++ i) {
			ans = std::max(ans, (a[i] - a[i-1])/2 + 1);
		}
		printf("%d\n", std::max(ans, n-a[m-1]+1));
	}
}
