#include <bits/stdc++.h>
const int M = 1e6;

int v[M+10], p[M], sump[M], m;


void prime(int n) {
    memset(v, 0, sizeof(v));
    for(int i = 2; i <= n; ++i) {
        if(!v[i]) v[i] = i, p[m++] = i;
        for(int j = 1; j <= m; ++ j) {
            if(p[j] > v[i] || p[j] > n/i) break;
            v[i*p[j]] = p[j]; //i*p[j]的最小质因子
        }
    }
    sump[0] = p[0];
    for(int i = 1; i < m; ++ i) {
        sump[i] = sump[i-1] + p[i];
    }
}

int main() {
    prime(M); 
    printf("%d\n", m);

    int amo; std::cin>>amo;
}