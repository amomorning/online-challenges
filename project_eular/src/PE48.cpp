#include <bits/stdc++.h>

typedef long long ll;

const ll mod = 1e10;
const ll digs = 1e5;

ll mulmod(ll n, ll m) {
    ll ans = 0;
    ll a = n/digs, b = n%digs;
    ll c = m/digs, d = m%digs;

    ans=(ans+(((a*digs)%mod)*d)%mod)%mod;
    ans=(ans+(((b*digs)%mod)*c)%mod)%mod;
    ans=(ans+b*d)%mod;
    return (ans+mod)%mod;
}

ll qkmod(ll a, ll n) {
    ll ret = 1;
    while(n) {
        if(n&1) ret = mulmod(ret, a);
        a = mulmod(a, a), n >>= 1;
    }
    return ret;
}


int main() {
    ll ans = 0;
    for(int i = 1; i <= 1000; ++ i) {
        ans += qkmod(i, i);
        ans %= mod;
        // std::cout << ans%mod << std::endl;
    }
    std::cout << ans%mod << std::endl;

    std::cout << qkmod(8, 8) << std::endl;
    int amo; std::cin>>amo;
}