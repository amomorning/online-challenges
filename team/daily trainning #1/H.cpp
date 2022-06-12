#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int M = 2e6+10;

int w[M], t[M];
ll dp[M];
int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i ++) {
        int x; scanf("%d", &x);
        scanf("%d%d", &w[x], &t[x]);
    }
    for(int i = M; i > 0; i --) {
        if(!dp[i]) dp[i] = dp[i+1];
        if(w[i]) {
            dp[i] = max(dp[i], dp[i+t[i]]+w[i]);
        }
    } 
    printf("%I64d\n", dp[1]);
}
