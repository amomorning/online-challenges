#include <bits/stdc++.h>

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    int cnt = 0;
    for(int i = 0; i < n; ++ i) {
        for(int j = 0; j < m; ++ j) {
            
            bool flag = false;
            for (int k = 0; k < 2; ++ k) {
                int a; scanf("%d", &a);
                if(a) flag = true; 
            }
            if(flag) cnt ++;
        }
    }
    printf("%d", cnt);
}
