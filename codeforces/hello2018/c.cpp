#include <bits/stdc++.h>
const int inf = 0x3f3f3f3f;
typedef long long ll;
ll c[55];

int main() {
    int n, L;
    scanf("%d%d", &n, &L);
    for(int i = 0; i < n; ++ i) scanf("%lld", &c[i]);
    for(int i = 1; i < n; ++ i) c[i] = std::min(c[i], 2ll*c[i-1]);
    for(int i = n-2; i >= 0; -- i) c[i] = std::min(c[i], c[i+1]);
    ll ans = 1e18, tmp = 0;
    for(int i = n-1; i >= 0; -- i) {
        tmp += c[i]*(L>>i);
        ans = std::min(ans, tmp+c[i]);
        L %= (1ll<<i); 
    }
    printf("%lld\n", std::min(ans, tmp));
}
