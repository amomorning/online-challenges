#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, a, b;
    scanf("%d%d%d", &n, &a, &b);
    int cnt = 0, c = 0;
    for(int i = 0; i < n; i ++) {
        int x;
        scanf("%d", &x);
        if(x == 2 && b) {
            b --;
        } else if(x == 1) {
            if(a) a --;
            else if(b) {
                b --;
                c ++;
            } else if(c) {
                c --;
            }else cnt ++;
        } else cnt += 2;
    }
    printf("%d\n", cnt);
}
