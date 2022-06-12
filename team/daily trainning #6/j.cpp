#include <bits/stdc++.h>
long long f[22];
bool check(long long x) {
	int cnt;
	for(cnt = 0; f[cnt] <= x; ++ cnt);
	cnt >>= 1;
	int a = 0, b = 0;
	a = x%f[cnt];
	b = x/f[cnt];
	if(a == 0 || b == 0) return 0;
	return std::__gcd(a, b) == 1;
}

int main() {
	int t; scanf("%d", &t);
	f[0] = 1;
	for(int i = 1; i < 19; ++ i) f[i] = f[i-1]*10ll;
	while(t --) {
		long long l, r;
		scanf("%lld%lld", &l, &r);
		long long ans = -1;
		for(long long i = r; i >= l; i --) {
			if(check(i)) {
				ans = i;
				break;
			}
		}
		printf("%lld\n", ans);
	}
}
