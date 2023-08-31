#include <bits/stdc++.h>

int main() {
	long long n;
	int m;
	scanf("%lld%d", &n, &m);
	for(int i = 0; i < m; ++ i) {
		long long x; scanf("%lld", &x);
		while(!(x&1)) {
			x = n+(x/2);
		}
		printf("%lld\n", (x+1)/2);
	}
}
