#include <bits/stdc++.h>
const int N = 1e5+10;

struct node{
    int v, pos;
    bool operator < (node o) {
        if(v == o.v) return pos < o.pos;
        return v < o.v;
    }
};
node b[N], c[N];
int a[N], vis[N];

int main() {
    int n; 
    while(~scanf("%d", &n)) {
        memset(vis, 0, sizeof(vis));
        for(int i = 0; i < n; ++ i) {
            scanf("%d", &a[i]);
        }
        for(int i = 0; i < n; ++ i) {
            int v; scanf("%d", &v);
            b[i] = {v, i};
        }
        std::sort(b, b+n);
        for(int i = 0; i < n; ++ i) {
            c[i] = {a[b[i].pos], i};
        }

        std::sort(c, c+n);
        int s = c[0].pos, t = c[s].pos;
        vis[0] = 1, vis[s] = 1;
        while(t != s) {
            vis[t] = 1;
            t = c[t].pos;
        }

        bool flag = false;
        for(int i = 0; i < n; ++ i) if(!vis[i]) flag = true;

        for(int i = 1; i < n; ++ i) {
            if(c[i].v <= b[i-1].v) flag = true;
        }
        for(int i = 0; i < n; ++ i) {
            if(c[i].v > b[i].v) flag = false;
        }
        if(flag) puts("Yes");
        else puts("No");
    }
}
