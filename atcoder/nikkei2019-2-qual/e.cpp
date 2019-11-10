#include <bits/stdc++.h>
const int N = 1e5;
int a[N];

int main() {
    int n, k; scanf("%d%d", &n, &k);
    if(n < k + k - 1) puts("-1");
    else {
        int t = 0;
        for(int i = 0; i < k; ++ i) {
            printf("%d %d %d\n", k+i,  n*2+i, k+i*2+n*2);
            a[t++] = k + i*2 + n*2 + 1;    
        }
        for(int i = 0; i < t && i+k < n; ++ i) {
            printf("%d %d %d\n", i+k*2, k+n+i, a[i]);
        }
        int tmp = 3*k+n*2;
        for(int i = k*2 + t; i < n+k; ++ i) {
            printf("%d %d %d\n", i, n-k+i, tmp++);
        }
    }
    int amo; std::cin >> amo;
}
