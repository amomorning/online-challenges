#include <bits/stdc++.h>
using namespace std;
const int N = 1e5+10;
const int mod = 1e9+7;

int a[N], c[N];
pair<int, int> b[N];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d", &n);
		for(int i = 1; i <= n; ++ i) {
			scanf("%d", &a[i]);
			b[i] = {a[i], i};
		}
		sort(b+1, b+1+n);
		memset(c, 0, sizeof(c));
		for(int i = 1; i <= n; ++ i) {
			if(i == b[n].second) c[i] = (a[i] + b[n-1].first)%mod;
			else c[i] = (a[i]+b[n].first)%mod;
			int p = lower_bound(b+1, b+1+n, make_pair(mod-a[i], 0)) - b;
			p --;
			if(b[p].second == i) p --;
			if(p > 0) c[i] = max(c[i], (a[i]+b[p].first)%mod);
		}
		for(int i = 1; i <= n; ++ i) {
			printf("%d%c", c[i], " \n"[i == n]);
		}
	}
}
