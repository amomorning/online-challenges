#include <bits/stdc++.h>
const int N = 2e5+10;
const int P = 146527;
const int mod = 1e9+9;
typedef unsigned long long ll;

ll hash[30][N], base[N];
ll a[30], b[30];
char s[N];

bool check() {
	std::sort(a, a+26);
	std::sort(b, b+26);
	for(int i = 0; i < 26; ++ i) 
		if(a[i] != b[i]) return false;
	return true;
}

int main() {
	int n, m; scanf("%d%d%s", &n, &m, s+1);
	base[0] = 1ll;
	for(int i = 1; i <= n; ++ i) base[i] = base[i-1]*P%mod;
	for(int i = 1; i <= n; ++ i) {
		for(int ch = 0; ch < 26; ++ ch) {
			hash[ch][i] = (hash[ch][i-1]*P%mod + (ch+'a' == s[i])+mod)%mod;
		}
	}	
	while(m --) {
		int x, y, len; scanf("%d%d%d", &x, &y, &len);
		for(int ch = 0; ch < 26; ++ ch) {
			a[ch] = (hash[ch][x+len-1] - hash[ch][x-1]*base[len]%mod + mod) %mod;
			b[ch] = (hash[ch][y+len-1] - hash[ch][y-1]*base[len]%mod + mod) %mod;
		}
		if(check()) puts("YES");
		else puts("NO");
	}
}
