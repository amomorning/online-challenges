#include <bits/stdc++.h>
using namespace std;
const int M = 1e5+10;
typedef long long ll;
ll w[M];
int vis[M], fa[M], D, t[M];
vector<int> G[M], L[M];

void dfs(int u, int f,int d) {
    D = max(D, d);
    vis[u] = 1;
    fa[u] = f;
    L[d].push_back(u);
    t[u] = 0;
    for(int i = 0; i < G[u].size(); i ++) {
        int v = G[u][i];
        if(vis[v] == 0) {
            dfs(v, u, d+1);
            w[u] += w[v];
            t[u] ++;
        }
    }
    return;
}

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; i ++) {
        scanf("%d", &w[i]);        
    }
    for(int i = 0; i < n-1; i ++) {
        int u, v;
        scanf("%d%d", &u, &v);
        G[u].push_back(v);
        G[v].push_back(u);
    }
    memset(vis, 0, sizeof(vis));
    D = -1;
    dfs(1, -1, 0);
    ll tot = w[1];
    for(int i = D-1; i >= 0; i --) {
        for(int j = 0; j < L[i].size(); j ++) {
            int u = L[i][j];
            int g = -1, b = 1, num = 0;
            ll mn = 1e14;
            for(int v : G[u]) {
                if(v != fa[u]) {
                    num++;
                    mn = min(mn, w[v]);
                    if(!t[v]) continue;
                    b *= t[v];
                    if(g == -1) g = t[v];
                    else g = __gcd(g, t[v]);
                }
            }
            if(num == 0) {
                continue;
            }
            if(b == 1) {
                w[u] = 1ll*num*mn;
                continue;
            }
            if(t[u] && b) t[u] = (t[u]*b);
            b /= g;
            if(b) w[u] = mn/b*b*num;
            else w[u] = 0;
        }
/*
        for(int j = 0; j < L[i].size(); j ++) {
            int u = L[i][j];
            printf("[%d] = %d, %d\n", u, w[u], t[u]);
        }
*/
    }
    /*
    for(int i = 1; i <= n; i ++) {
        printf("%d ", t[i]);
    }
    puts("");
    */
    printf("%I64d\n", tot-w[1]);
}
