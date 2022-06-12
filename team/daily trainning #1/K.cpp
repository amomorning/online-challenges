#include <bits/stdc++.h>
using namespace std;
const int M = 1e3+10;
const double eps = 1e-7;
int x[M], y[M], r[M], vis[M];
vector<int> G[M];
int flag;

double dis(int i, int j) {
    return sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]));
}

void dfs(int u, int f) {
    if(vis[u] == f) return;
    if(vis[u] == !f) {flag = 0; return;}
    vis[u] = f;
    for(int i = 0; i < G[u].size(); i ++) {
        int v = G[u][i];
        dfs(v, !f);
    }
    return;
} 

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i ++) {
        scanf("%d%d%d", &x[i], &y[i], &r[i]);
    }
    for(int i = 0; i < n; i ++) {
        for(int j = i+1; j < n; j ++) {
            if(dis(i, j) - 1.0*(r[i] + r[j]) < eps) {
                G[i].push_back(j);
                G[j].push_back(i);
            }
        }
    }
    flag = 1;
    memset(vis, -1, sizeof(int)*(n+1));
    dfs(0, 0);
    if(!flag) 
        puts("The input gear cannot move.");
    else if(vis[n-1] == -1) 
        puts("The input gear is not connected to the output gear.");
    else {
        int g = __gcd(r[n-1], r[0]);
        if(vis[n-1] == 0) printf("%d:%d\n", r[0]/g, r[n-1]/g);
        else printf("-%d:%d\n", r[0]/g, r[n-1]/g);
    }
}
