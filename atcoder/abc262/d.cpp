#include <stdio.h>
const int MOD = 998244353;
const int MAX = 101;

int a[MAX];

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; ++ i) {
        scanf("%d", &a[i]);
    }
    int tot = 0;

    for (int m = 1; m <= n; ++ m) {
        int dp[n+1][n+1][n];
        for(int i = 0; i < n+1; ++ i) {
            for(int j = 0; j < n+1; ++ j) {
                for(int k = 0; k < n; ++ k) {
                    dp[i][j][k] = 0;
                }
            }
        }
        dp[0][0][0] = 1;

        for(int i = 0; i < n; ++ i) {
            for(int j = 0; j < n; ++ j) {
                for(int k = 0; k < n; ++ k){
                    dp[i+1][j+1][(k+a[i])%m] = (dp[i+1][j+1][(k+a[i])%m] + dp[i][j][k]) % MOD;
                    dp[i+1][j][k] = (dp[i+1][j][k] + dp[i][j][k]) % MOD;
                }
            }
        }

        tot = (tot + dp[n][m][0]) % MOD;
        
    }
    printf("%d\n", (tot%MOD+MOD)%MOD);
}
