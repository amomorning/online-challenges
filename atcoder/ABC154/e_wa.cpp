#include <bits/stdc++.h>

typedef long long ll;
std::string s;
int k;
int dim[111];
int f[111][5];

int dfs(int x, int st, int op) {
    if(!op && !x) return 1;
    if(!op && ~f[x][st]) return f[x][st];

    int ret = 0;
    int mx = op ? dim[x] : 9;
    for(int i = 0; i <= mx; ++ i) {
        if(i) ret += dfs(x-1, st-1, op & (i == mx));
        else ret += dfs(x-1, st, op && (i == mx));
    } 
    if(!op) f[x][st] = ret;
    return ret;
}
int main() {
    std::cin >> s >> k;
    int n = s.size();
    for(int i = 0; i < n; ++i) {
        dim[i] = s.at(i) - '0';
    }

    memset(f, -1, sizeof f);
    // std::cout << dfs(n-1, k, 1) << std::endl;
    std::cout << dfs(n-1, k, 0)<< std::endl;

    for(int i = 0; i < n; ++ i) {
        for(int j = 0; j <= k; ++ j) {
            printf("f[%d][%d] = %d\n", i, j, f[i][j]);
        }
    }
    int amo; std::cin >> amo;
}
