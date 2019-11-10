#include <bits/stdc++.h>
typedef long long ll;
int lim = 1e5;
ll n, k;
int id;
ll ans[100001];
std::map<ll, std::vector<ll> > mp;

void dfs(ll n, int deep) {
	if(id == lim) return;
	if(mp.find(n) == mp.end()) {
		for(int i = 1; 1ll*i*i <= n; ++ i) if(n%i == 0) {
			mp[n].push_back(i);
			if(n/i != i) mp[n].push_back(n/i);
		}
		std::sort(mp[n].begin(), mp[n].end());
	}
	if(deep == k) {
		for(auto x: mp[n]) {
			ans[id++] = x;
			if(id == lim) break;
		}
		return;
	}
	for(auto x: mp[n]) {
		if(x != 1) dfs(x, deep+1);
		else ans[id++] = 1;
		if(id == lim) break;
	}
}

int main() {
	scanf("%lld%lld", &n, &k); 
	if(k == 0) return printf("%lld", n), 0;
	if(k >= 1e5 && n != 1) {
		for(int i = 0; i < lim; i ++) printf("1 ");
		return 0;
	}
	id = 0;
	dfs(n, 1);
	for(int i = 0; i < id; ++ i) printf("%lld ", ans[i]);
}
