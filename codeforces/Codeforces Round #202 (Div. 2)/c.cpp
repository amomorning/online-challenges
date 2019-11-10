#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int M = 1e5+10;
  
ll a[M];
int n;

bool c(ll r) {
    ll tot = 0;
    for(int i = 0; i < n; i ++) {
        tot += (r-a[i]);
    }
    return tot >= r;
}

int main() {
    scanf("%d", &n);
    ll L = -1, R = 1e10;
    for(int i = 0; i < n; i ++) {
        scanf("%I64d", &a[i]);
        L = max(L, a[i]);
    }
    while(L < R) {
        ll mid = (L+R)/2;
        if(c(mid)) R = mid;
        else L = mid + 1;
    }
    printf("%I64d\n", R);
}
