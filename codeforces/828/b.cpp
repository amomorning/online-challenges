#include <bits/stdc++.h>
using namespace std;
char s[110];
int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    int mx = -1, my = -1, nx = 110, ny = 110;
    int cnt = 0;
    for(int i = 0; i < n; i ++) {
        scanf("%s", s);     
        for(int j = 0; j < m; j ++) {
            if(s[j] == 'B') {
                nx = min(nx, i);
                ny = min(ny, j);
                mx = max(mx, i);
                my = max(my, j);
                cnt ++;
            }
        }
    }
    //printf("%d %d %d %d\n", nx, mx, ny, my);
    if(cnt == 0) return puts("1"),0;
    int a = max(my - ny + 1, mx - nx + 1);
    if(n < a || m < a) puts("-1");
    else printf("%d\n", a*a-cnt);
}
