#include <bits/stdc++.h>

int a[111];
int dp[111][5][2];

std::string s;
int k, N;

int nR(int n, int r) {
    if(n > N) return 0;
    if(r == 1) return n;
    if(r == 2) return n * (n - 1) / 2;
    if(r == 3) return n * (n - 1) * (n - 2) / 6;
    return 0;
}

long long dfs(int i, int st, int op) {
    if(i == N) {
        if(st == 0) return 1;
        else return 0;
    }
    if(st == 0) return 1;

    if(op) return nR(N-i, st) * pow(9, st);
    else {
        return dfs(i+1, k, 1)
                + dfs(i+1, k-1, 1) * (s[i] - '1')
                + dfs(i+1, k-1, 0);
    }
}
int main() {
    std::cin >> s >> k;
    N = s.size();
    std::cout << dfs(0,k,0) << std::endl;

    int amo; std::cin >> amo;
}
