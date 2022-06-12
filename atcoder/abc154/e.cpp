#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

string s;
int n, k;
ll dp[101][5][2];
int main() {
    cin >> s >> k;
    n = s.size();
    dp[0][0][0] = 1; 

    for(int i = 0; i < n; i++) {
        for(int j = 0; j <= k; j++) {
            // op = 0 = 
            if(s[i] == '0') dp[i+1][j][0] += dp[i][j][0];
            else {
                dp[i+1][j][1] += dp[i][j][0];
                dp[i+1][j+1][0] += dp[i][j][0];
                dp[i+1][j+1][1] += dp[i][j][0]*(s[i]-'1');
            }

            // op = 1 <
            dp[i+1][j][1] += dp[i][j][1];
            dp[i+1][j+1][1] += dp[i][j][1] * 9;
        }
    }

    cout << dp[n][k][0] + dp[n][k][1] << endl;
    int amo; std::cin >> amo;
}
