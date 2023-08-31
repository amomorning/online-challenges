#include <bits/stdc++.h>
const int M = 1e3+10;
const int mod = 1e9+7;
typedef long long ll;
char s[M];
int a[M];
ll c[M][M];

void init() {
	for(int i = 0; i < M; i ++) {
		c[i][0] = c[i][i] = 1ll;
		for(int j = 1; j < i; j ++) {
			c[i][j] = c[i-1][j] + c[i-1][j-1];
			c[i][j] %= mod;
		}
	}
}
int len;

void convert() {
	len = 0;
	int l = strlen(s);
	for(int k = 0; k < l; k ++) {
		int t = s[k] - '0';
		int cnt = 0;
		while(t) {
			a[cnt] += t%2;
			int tmp = cnt;
			while(a[tmp] > 1) {
				a[tmp++] = 0;
				a[tmp] ++;
				len = std::max(len, tmp);
			}
			t /= 2;
			cnt ++;
		}	
		if(!len) len = cnt-1;
		if(k == l-1) continue;
		
		int mxlen= len;
		for(int i = len+2; i >= 2; -- i) {
			a[i] += a[i-2];
			int t = i;
			mxlen = std::max(mxlen, t);
			while(a[t] > 1) {
				a[t++] = 0;
				a[t] ++;
				mxlen = std::max(mxlen, t);
			}
		}
		len = mxlen+1;
		for(int i = len; i > 0; -- i) 
			a[i] = a[i-1];
		a[0] = 0;
	}
}

int main() {
	int k;
	scanf("%s%d", s, &k);
//	convert();	
	len = strlen(s);
	for(int i = 0; s[i]; i ++) a[i] = s[i] - '0';
	init();
	int cnt = 0;
	ll ans = 0;
	for(int i = 0; i <= len; i ++) {
		if(a[i]) {
			ans += c[len-i-1][k-cnt];
			printf("%lld\n", ans);
			ans %= mod;
			cnt ++;
		}
	}	
	printf("%lld\n", ans);
}
