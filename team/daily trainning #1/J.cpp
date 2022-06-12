#include <bits/stdc++.h>
using namespace std;

int dx[10] = {0, 0, 0, 1, 1, 1, -1, -1, -1};
int dy[10] = {0, 1, -1, 0, 1, -1, 0, 1, -1};
int a[110][110], b[110][110];

int n, m, t;
void solve(int x, int y) {
    int tot = 0;
    for(int i = 0; i < 9; i ++) {
        int xx = (x+dx[i]+m)%m;
        int yy = (y+dy[i]+n)%n;
        tot += a[xx][yy];
    }
    //printf("tot == %d\n", tot);
    b[x][y] = tot/9;
}

int main() {
    scanf("%d%d%d", &n, &m, &t);
    for(int i = 0; i < m; i ++) {
        for(int j = 0; j < n; j ++) {
            scanf("%d", &a[i][j]);
            a[i][j] *= 9;
        } 
    }
    while(t --) {
        for(int i = 0; i < m; i ++) {
            for(int j = 0; j < n; j ++) {
                solve(i, j);
            }
        }
        for(int i = 0; i < m; i ++) {
            for(int j = 0; j < n; j ++) {
                a[i][j] = b[i][j]*9;
            }
        }
    }
    set<int> st;
    for(int i = 0; i < m; i ++) {
        for(int j = 0; j < n; j ++) {
            st.insert(a[i][j]);
        }
    }
    printf("%d\n", st.size());
}
