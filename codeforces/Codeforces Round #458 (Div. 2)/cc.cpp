#include <bits/stdc++.h>
const int M = 1e3+10;
const int mod = 1e9+7;
typedef long long ll;

int a[M];
ll c[M][M];
char s[M];

int bit(int k) {
	int cnt = 0;
	while(k) {
		if(k&1) cnt ++;
		k >>= 1;
	}
	return cnt;
}


void init() {
	for(int i = 0; i < M; i ++) {
		c[i][0] = c[i][i] = 1ll;
		for(int j = 1; j < i; j ++) {
			c[i][j] = c[i-1][j] + c[i-1][j-1];
			c[i][j] %= mod;
		}
	}
}

int main() {
	a[1] = 1;
	for(int i = 2; i < M; i ++)  {
		a[i] = a[bit(i)] + 1;
	}
	std::vector<int> v[M];
	for(int i = 1; i < M; i ++) {
		v[a[i]].push_back(i);
	}
	int k;
	init();
	scanf("%s%d", s, &k);
	if(k == 0) return puts("1"), 0;
	ll ans = 0;
	for(int x:v[k]) {
		int cnt = 0;
		int len = strlen(s);
		for(int i = 0; i < len; i ++) {
			if(s[i]-'0') {
				if(x >= cnt) ans += c[len-i-1][x-cnt];
				ans %= mod;
				cnt ++;
			}
		}
		if(cnt == x) ans ++;
	}
	if(k == 1) ans --;
	printf("%lld\n", (ans+mod)%mod);
}
