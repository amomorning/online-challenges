#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9+7;
const int N = 2e5+10;
typedef long long ll;

ll qkmod(ll a, ll n) {
	ll ret = 1;
	while (n) {
		if(n & 1) ret = ret*a%MOD;
		a = a*a%MOD, n >>= 1;
	}
	return ret;
}

ll Inv(ll x, ll p) {
	return qkmod(x, p-2);
}

int F[N], Finv[N], inv[N];//F是阶乘，Finv是逆元的阶乘 
void init(){
	inv[1] = 1;
	for(int i = 2; i < N; i ++){
		inv[i] = (MOD - MOD / i) * 1ll * inv[MOD % i] % MOD;
	}
	F[0] = Finv[0] = 1;
	for(int i = 1; i < N; i ++){
		F[i] = F[i-1] * 1ll * i % MOD;
		Finv[i] = Finv[i-1] * 1ll * inv[i] % MOD;
	}
}

int comb(int n, int m){//comb(n, m)就是C(n, m) 
	if(m < 0 || m > n) return 0;
	return F[n] * 1ll * Finv[n - m] % MOD * Finv[m] % MOD;
}

int main() {
	int t; scanf("%d", &t);
	init();
	while(t --) {
		int n, m; scanf("%d%d", &n, &m);
		if(n+m < 0 || abs(m-n)%2 != 0) {
			puts("0");
			continue;
		}
		printf("%lld\n", (1ll*comb(m, (n+m)/2)*Inv(qkmod(2,m), MOD)%MOD+MOD)%MOD);
	}
}
