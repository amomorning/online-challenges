#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9+7;
typedef long long ll;
const int N = 1e5+10;

int _gcd(int a, int b) {
	return b?_gcd(b, a%b):a;
}

ll qkmod(ll a, ll n) {
	ll ret = 1;
	while(n) {
		if(n&1) ret = ret*a%MOD;
		a = a*a%MOD, n >>= 1;
	}
	return ret;
}

ll Inv(ll x, ll p = MOD) {
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
	int m, n, k;
	double p; 
	init();
	scanf("%d%d%d%lf", &m, &n, &k, &p);
	int gcd = _gcd(1000*p, 1000);
	int pl = p*1000/gcd;
	int pr = 1000/gcd;
 // printf("%d\n", comb(n-1, k-1));
	 if(k > n) puts("0");
	else printf("%lld\n", comb(n-1, k-1)*qkmod(pl, k)%MOD*qkmod(pr-pl, n-k)%MOD*Inv(qkmod(pr, n))%MOD);	
}
