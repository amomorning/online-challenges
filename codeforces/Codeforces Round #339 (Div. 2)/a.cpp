#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll M = 1e18+10;

int main() {
    int l, r, k;
    scanf("%d%d%d", &l, &r, &k);
    bool flag = false;
    for(ll i = 1; i < M; i *= k) {
        if(i >= l && i <= r) {
            flag = true;
            printf("%I64d ", i);
        }
    }
    if(!flag) puts("-1");
}
