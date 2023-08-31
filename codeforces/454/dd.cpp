#include <bits/stdc++.h>
const int inf = 0x3f3f3f3f;
const int N = 17;
const int M = 110;

int a[M], prime[M], stat[M];
int dp[M][1<<N];
std::pair<int, int> pre[M][1<<N];

bool is_prime(int x) {
	if(x == 1) return false;
	if(x == 2) return true;
	for(int i = 2; i*i <= x; i ++) {
		if(x%i == 0) return false;
	}
	return true;
}

void init() {
	int cnt = 0;
	for(int i = 2; i < 100; i ++) {
		if(is_prime(i)) prime[cnt++] = i;
	}
	for(int i = 1; i < 100; i ++) {
		for(int j = 0; j < cnt; j ++) if(i%prime[j] == 0) {
			stat[i] |= (1<<j);
			// printf("pr[%d] = %d\n", j, prime[j]);
		}
		// std::cout << "i = " <<i << " : " << stat[i] << std::endl;
	}
}


int main() {
	int n;
	std::cin >> n;
	init();
	for(int i = 1; i <= n; i ++) std::cin >> a[i];
	memset(dp, 0x3f, sizeof(dp));
	for(int i = 0; i < (1<<17); i ++) 
		dp[0][i] = 0;
	for(int i = 1; i <= n; i ++) {
		for(int k = 1; k <= 60; k ++) {
			int x = (~stat[k])&((1<<N)-1);
			for(int s = x; s; s = (s-1)&x) {
				if(dp[i-1][s] != inf && dp[i-1][s] + abs(a[i]-k) < dp[i][s|stat[k]]) {
					dp[i][s|stat[k]] = dp[i-1][s] + abs(a[i]-k);
					pre[i][s|stat[k]] = {s, k};
				}
			}
		}
	}
	int s = 0;
	for(int i = 0; i < (1<<17); i ++) {
		if(dp[n][i] < dp[n][s]) s = i;
	}
	std::vector<int> ans;
	for(int i = n; i; i --) {
		ans.push_back(pre[i][s].second);
		s = pre[i][s].first;
	}
	std::reverse(ans.begin(), ans.end());
	for(auto x : ans) printf("%d ", x);
}
