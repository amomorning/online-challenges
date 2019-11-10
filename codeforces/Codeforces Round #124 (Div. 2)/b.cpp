#include <bits/stdc++.h>
using namespace std;
int a[110], b[110];

int main() {
    int n, m; scanf("%d%d", &n, &m);
    for(int i = 0; i <= n; i ++) {
        scanf("%d", &a[i]);    
    }
    for(int i = 0; i <= m; i ++) {
        scanf("%d", &b[i]);
    }
    if(m > n) return puts("0/1"), 0;
    if(a[0]*b[0] < 0) printf("-");
    if(m < n) {
        return puts("Infinity"), 0;
    }
    int g = __gcd(abs(a[0]), abs(b[0]));
    printf("%d/%d\n", abs(a[0])/g, abs(b[0])/g);
}
