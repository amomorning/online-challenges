#include <bits/stdc++.h>
typedef long long ll;
int f[11];

bool check(ll x) {
	ll r = x; 
	int len = 0;
	while(r) {r/=10; len ++;}
	int a = x/f[len/2];
	int b = x%f[len/2];
	// printf("%d %d\n", a, b);
	if(a == 0 || b == 0) return 0;
	return std::__gcd(a, b) == 1;
}

int main() {
	int t; scanf("%d", &t);
	f[0] = 1;
	for(int i = 1; i < 10; ++ i) f[i] = f[i-1] * 10;
	while(t --) {
		ll l, r;
		scanf("%lld%lld", &l, &r);	
		ll ans = -1;
		for(ll i = r; i >= l; i --) {
			if(check(i)) {
				ans = i;
				break;
			}
		}
		printf("%lld\n", ans);
	}
}
