#include <bits/stdc++.h>
#define P pair<int,int> 
using namespace std;
const int M = 1500+10;
int dx[5] = {0, 0, 1, -1};
int dy[5] = {1, -1, 0, 0};
char mp[M][M];
P vis[M][M];


int n, m;
bool bfs(P s) {
    for(int i = 0; i < n; i ++) for(int j = 0; j < m; j ++) {
        vis[i][j] = P(-1, -1);
    }
    queue<P> q;
    q.push(s);
    while(!q.empty()) {
        P p = q.front(); q.pop();
        int x = p.first;
        int y = p.second;
        int mx = (x%n+n)%n;
        int my = (y%m+m)%m;
        if(vis[mx][my] == P(-1, -1)) vis[mx][my] = P(x, y);
        else if(vis[mx][my] != P(x, y)) return true;     
        else continue;
        for(int i = 0; i < 4; i ++) {
            int nx = x+dx[i];
            int ny = y+dy[i];
            int mx = (nx%n+n)%n;
            int my = (ny%m+m)%m;
            if(vis[mx][my] != P(nx, ny) && mp[mx][my] != '#') {
                q.push(P(nx, ny));
            }
        }
    }
    return false;
}

int main() {
    scanf("%d%d", &n, &m);
    P s;
    for(int i = 0; i < n; i ++) {
        scanf("%s", mp[i]);
        for(int j = 0; mp[i][j]; j ++) {
            if(mp[i][j] == 'S') s=P(i, j);
        }
    }
    if(bfs(s)) puts("Yes");
    else puts("No");
}
