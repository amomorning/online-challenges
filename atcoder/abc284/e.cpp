#include <bits/stdc++.h>
const int MAX = 2e5+10;
int vis[MAX];
std::vector<int> G[MAX];
int tot = 0;

void dfs(int u) {
    if(tot >= 1e6) return;
    vis[u] = 1;

    tot ++;
    if(tot >= 1e6) return;

    for(int i = 0; i < G[u].size(); ++i) {
        int v = G[u][i];
        if (vis[v] == 0) dfs(v);
    }

    vis[u] = 0;
}

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    for(int i = 0; i < m; ++ i) {
        int u, v;
        scanf("%d%d", &u, &v);
        u--; v--;
        G[u].push_back(v);
        G[v].push_back(u);
    }
    
    dfs(0);
    printf("%d\n", tot);
}
    
