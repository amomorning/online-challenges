#include <bits/stdc++.h>
using namespace std;

void dfs1(int u, int pre) {
    fa[u] = pre;
    vis[u] = 1;
    for(int i = 0; i < G[u].size(); i ++) {
        int v = G[u][i];
        if(v == pre) continue;
        dfs(v, u);
        t[u] ++;
        w[u] += w[v];
    }
}

void dfs2(int u) {
    int g = 1, b = 1;
    int tot = G[u].size() - 1;
    ll mn = 1e14;
    ll mx = -1;
    for(int i = 0; i < G[u].size(); i ++) {
        int v = G[u][i];
        if(v == fa[u]) continue;
        dfs2(v);
        mn = min(mn, w[v]);
        mx = max(mx, w[v] - a[v]);
        if(!t[v]) continue;
        b *= t[v];
        if(g == 1) g = t[v];
        else g = __gcd(g, t[v]);
    }
    if(!tot) return;
    b /= g;
    if(mn > mx) {
        w[u] = 1ll*mn*tot + a[u];
        return;
    } 
    t[u] = b*tot;
    for(int i = 0; i < G[u].size(); i ++) {
        int v = G[u].size();
        if(v == fa[u]) continue;
            
    }
}

int main() {
    int n; scanf("%d", &n);
    for(int i = 1; i <= n; i ++) {
        scanf("%d", &w[i]);
        a[i] = w[i];
    }
    for(int i = 1; i < n; i ++) {
        int u, v; scanf("%d%d", &u, &v);
        G[u].push_back(v);
        G[v].push_back(u);
    }
    memset(vis, 0, sizeof(vis));
    dfs1(1, -1);
    memset(vis, 0, sizeof(vis));
    int ans = w[1];
    dfs2(1);
}
