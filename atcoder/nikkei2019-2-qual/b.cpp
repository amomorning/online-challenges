#include <bits/stdc++.h>
const int N = 1e5 + 10;
const int mod = 998244353;
int a[N];
typedef long long ll;

ll qk_mod(ll a, ll n) {
    ll ret = 1;
    while(n) {
        if(n&1) ret = ret*a%mod;
        a = a*a%mod, n >>= 1;
    }
    return ret;
}

int main() {
    int n; scanf("%d", &n);
    int mxd = 0, first;
    for(int i = 1; i <= n; ++ i) {  
        int x; scanf("%d", &x);
        if(i == 1) first = x;
        a[x] ++;
        mxd = std::max(mxd, x);
    }
    ll tot = 1;
    for(int i = 0; i < mxd; ++ i) {
        if(a[i] == 0) {
            tot = 0;
            break;
        }
        tot *= qk_mod(a[i], a[i+1]);
        tot %= mod;
    }
    if(a[0] != 1 || first != 0) tot = 0;
    std::cout << (tot+mod)%mod << std::endl;
    int amo; std::cin >> amo;
}
