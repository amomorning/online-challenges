#include <bits/stdc++.h>
const int N = 1e5+10;
const int mod = 1e9+7;

long long a[N], s[N];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d", &n);
		for(int i = 1; i <= n; ++ i) scanf("%lld", &a[i]);
		s[0] = 0;
		for(int i = 1; i <= n; ++ i) {
			s[i] = s[i-1] + a[i] * s[i-1] + a[i];
			s[i] %= mod;
		}
		printf("%lld\n", s[n]);
	}	
}
