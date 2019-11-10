#include <bits/stdc++.h>
const int M = 1e3+10;
std::vector<int> G[M];

bool flag = true;

void dfs(int u, int p) {
    int cnt = 0;
    for(int i = 0; i < G[u].size(); i ++) {
        int v = G[u][i];
        if(v == p) continue;
        if(G[v].size() == 1) cnt ++;
        else dfs(v, u);
    }
    if(cnt < 3) flag = false;
}

int main() {
    int n; scanf("%d", &n);
    for(int i = 1; i < n; ++ i) {
        int p;
        scanf("%d", &p); p --;
        G[p].push_back(i);
        G[i].push_back(p);
    } 
    dfs(0, -1);
    if(flag) puts("Yes");
    else puts("No");
}
