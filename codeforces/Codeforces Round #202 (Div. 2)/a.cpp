#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    int c[3] = {0};
    bool flag = true;
    for(int i = 0; i < n; i ++) {
        int x; scanf("%d", &x);
        if(!flag) continue;
        if(x == 25) {
            c[0] ++;
        }
        if(x == 50) {
            if(!c[0]) flag = false;
            c[1] ++;
            c[0] --;
        }
        if(x == 100) {
            if(!c[0]) flag = false;
            if(c[1]) {
                c[1] --;
                c[0] --;
            } else {
                if(c[0] < 3) flag = false;
                c[0] -= 3;
            }
            c[2] ++;
        }
    }
    if(flag) puts("YES");
    else puts("NO");
}
