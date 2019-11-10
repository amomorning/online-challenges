#include <bits/stdc++.h>
using namespace std;
int n, m;
const int INF = 0x3f3f3f3f;
const int M = 510;
int dx[5] = {0, 0, 1, -1};
int dy[5] = {1, -1, 0, 0};

int mp[M][M], vis[M][M];
char s[M];

bool check(int x, int y) {
    if(x < 1 || y < 1) return false;
    if(x > n || y > m) return false;
    if(vis[x][y] != INF) return false;
    return true;
}


void bfs() {
    queue<pair<int,int> > q;
    q.push({1,1});
    memset(vis, INF, sizeof(vis));
    vis[1][1] = 0;
    while(!q.empty()) {
        pair<int,int> u = q.front(); q.pop();
        //printf("DD%d %d\n", u.first, u.second);
        for(int i = 0; i < 4; i ++) {
            int x = u.first + mp[u.first][u.second]*dx[i];
            int y = u.second + mp[u.first][u.second]*dy[i];
            //printf("PP%d %d\n", x, y);
            if(check(x, y)) {
                q.push({x, y});
                vis[x][y] = min(vis[x][y], vis[u.first][u.second]+1);
            } 
        }
    }
    if(vis[n][m] == INF) puts("IMPOSSIBLE");
    else printf("%d\n", vis[n][m]);
}

int main() {
    scanf("%d%d", &n, &m);
    for(int i = 1; i <= n; i ++) {
        scanf("%s", s);
        for(int j = 0; j < m; j ++) {
            mp[i][j+1] = s[j] - '0';
        }
    }

    bfs();
}
