#include <bits/stdc++.h>
using namespace std;
const int M = 1e5+10;
#define pii pair<int, int>

pii a[M];

int main() {
    int v;
    scanf("%d", &v);
    int mx = 0, mxi;
    for(int i = 1; i < 10; i ++) {
        int d;
        scanf("%d", &d); 
        a[i] = pii(d, v%d);
        if(v/d > mx) {
            mx = v/d;
            mxi = i;
        } else if(v/d == mx && v%d > a[mxi].second) mxi = i;
    } 
    if(mx == 0) return puts("-1"), 0;
    int yu = a[mxi].second;
    for(int i = 0; i < mx; i ++) {
        for(int k = 9; k >= mxi; k --) {
            int d = a[k].first - a[mxi].first;
            if(yu >= d) {
                printf("%d", k);
                yu -= d;
                break;
            }
        }
    }
    puts("");
    return 0;
}
