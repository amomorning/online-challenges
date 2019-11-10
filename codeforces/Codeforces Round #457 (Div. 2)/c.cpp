#include <bits/stdc++.h>
const int mod = 1e5+3;
const int M = 1e9;

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    if(m == 1) {
        return printf("%d %d\n%d %d %d\n", 2, 2, 1, 2, 2), 0;
    }
    printf("2 %d\n", mod);
    printf("%d %d %d\n", 1, n, 2);
    printf("%d %d %d\n", 1, 2, mod-n+1);
    for(int i = 3; i < n; i ++) {
        printf("%d %d %d\n", 1, i, 1);
    }
    m -= n-1;
    int tmp = n-1;
    while(m) {
        if(m < tmp) {
            int s = n-tmp+1;
            for(int i = s+1; i <= s+m; i ++) {
                printf("%d %d %d\n", s, i, M);
            }
            break;
        } else {
            int s = n-tmp+1;
            for(int i = s+1; i <= n; i ++) {
                printf("%d %d %d\n", s, i, M);
            }
            tmp --;
            m -= tmp;
        }
    }
}
