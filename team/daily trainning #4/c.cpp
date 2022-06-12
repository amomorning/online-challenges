#include <bits/stdc++.h>
using namespace std;
const int N = 1e5+10;
const int mod = 1e9+7;

int a[N], b[N], c[N];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d", &n);
		for(int i = 0; i < n; ++ i) {
			scanf("%d", &a[i]);
			b[i] = a[i];
		}
		sort(b, b+n);
		memset(c, 0, sizeof(c));
		for(int i = 0; i < n; ++ i) {
			int p = lower_bound(b, b+n, mod-a[i])-b;
			p --;
			if(p >= 0 && b[i] != a[i]) c[i] = (a[i] + b[p])%mod;
			else if(p > 0) c[i] = (a[i]+b[p-1])%mod;
			else if(i != n-1) c[i] = (a[i]+b[n-1])%mod;
			else c[i] = (a[i] + b[n-2])%mod;
		}
		for(int i = 0; i < n; ++ i) {
			printf("%d%c", c[i], " \n"[i+1 == n]);
		}
	}
}
