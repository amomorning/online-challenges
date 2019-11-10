#include <bits/stdc++.h>
typedef long long ll;

ll n, m, k;

bool c(ll x) {
	ll cnt = 0;
	for(int i = 1; i <= n; i ++) {
		cnt += std::min(m, x/i);
	}
	return cnt < k;
}

int main() {
	scanf("%lld%lld%lld", &n, &m, &k);
	ll l = 1, r = n*m;
	while(l <= r) {
		ll mid = (l+r) >> 1;
		if(c(mid)) l = mid + 1;
		else r = mid - 1;
	}
	printf("%lld\n", r+1);
}
