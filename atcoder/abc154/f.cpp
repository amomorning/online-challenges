#include <bits/stdc++.h>
const int N = 2e6+10;
const int MOD = 1e9+7;

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

int g(int r, int c) {
    int ret = 0;
    for(int i = 1; i <= c; ++ i) {
        ret = (ret + comb(i+r+1, r)) % MOD;
    }
    return ret;
}

int main() {
    init();
    int r1, c1, r2, c2;
    scanf("%d%d%d%d", &r1, &c1, &r2, &c2);
    int ans = (g(r2, c2) - g(r1-1, c2))%MOD +  (g(r1-1, c1-1) - g(r2, c1-1))% MOD;
    printf("%d\n", (ans%MOD+MOD)%MOD);

    int amo; std::cin >> amo;
}
