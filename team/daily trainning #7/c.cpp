#include <bits/stdc++.h>

int main() {
	long long a, b; scanf("%lld%lld", &a, &b);
	long long mx = std::max(a, b);
	long long ans = 0;
	for(int i = 1; 1ll*i*i <= mx; ++ i) {
		long long tmp = (b/i - ((a-1)/i));
		ans += tmp*i;
		ans += (b/i+((a-1)/i+1))*tmp/2;
		printf("%d - %lld %lld %lld\n", i, b/i, ((a-1)/i+1), tmp);
	}
	printf("%lld\n", ans);
}
