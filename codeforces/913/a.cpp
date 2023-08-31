#include <bits/stdc++.h>

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    int t = 1;
    while(n && m >= t) {
        t *= 2;
        n --;
    }
    printf("%d\n", m%t);
}
