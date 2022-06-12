#include <bits/stdc++.h>
const int M = 2e5+10;

long long a[M], b[M];

int main() {
	int n, m; scanf("%d%d", &n, &m);
	for(int i = 0; i < n; ++ i) {
		scanf("%lld", &a[i]);
		if(i) a[i] += a[i-1];
	}
	for(int i = 0; i < m; ++ i) {
		scanf("%lld", &b[i]);
		int pos = std::lower_bound(a, a+n, b[i]) - a;
		// printf("%d\n", a[pos]);
		if(pos) printf("%d %lld\n", pos+1, b[i]-a[pos-1]);
		else printf("%d %lld\n", pos+1, b[i]);
	}
}
