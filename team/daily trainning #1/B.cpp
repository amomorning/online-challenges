#include <bits/stdc++.h>
using namespace std;

char op[11][20];
int a[11];

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i ++) {
        scanf("%s%d", op[i], &a[i]);
    }
    int ans = 0;
    for(int i = 1; i <= 100; i ++) {
        int t = i;
        int flag = 1;
        for(int j = 0; j < n; j ++) {
            if(op[j][0] == 'A') t += a[j];
            if(op[j][0] == 'S') {
                t -= a[j];
                if(t < 0) {flag = 0; break;}
            }
            if(op[j][0] == 'M') {
                t *= a[j];
            }
            if(op[j][0] == 'D') {
                if(t%a[j] == 0) {
                    t /= a[j];
                } else {
                    flag = 0;
                    break;
                }
            }
        }
        if(!flag) ans ++;
    }
    printf("%d\n", ans);
}
