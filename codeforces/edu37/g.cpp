#include <bits/stdc++.h>
const int N = 1e6+10;
const int inf = 0x3f3f3f3f;

std::vector<int> fac[N];

void init() {
	for(int i = 1; i < N; i ++) {
		int n = i;
		for(int x = 2; 1ll*x*x <= n; ++ x) if(n%x == 0) {
			fac[i].push_back(x);
			while(n%x == 0) n/=x;
		}
		if(n != 1) fac[i].push_back(n);
	}
}

// get the number of y between 1~x such that gcd(y, p) == 1;
int get(int x, int p) {
	int tot = x;
	int t = fac[p].size();
	for(int i = 1; i < (1<<t); ++ i) {
		int cnt = 0, nu = 1;
		for(int j = 0; j < t; ++ j) {
			if(i&(1<<j)) {
				cnt ++;
				nu *= fac[p][j];
			}
		}
		if(cnt&1) tot -= x/nu;
		else tot += x/nu;
	}
	return tot;
}

int main() {
	init();
	int t; scanf("%d", &t);
	while(t --) {
		int x, p, k;
		scanf("%d%d%d", &x, &p, &k);
		int l = x, r = inf;
		while(l <= r) {
			int mid = (l+r) >> 1;
			if(get(mid, p)-get(x, p) >= k) r = mid-1;
			else l = mid + 1;
		}
		printf("%d\n", r+1);
	}
}
