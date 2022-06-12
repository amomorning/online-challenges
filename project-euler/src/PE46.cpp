#include <bits/stdc++.h>
const int M = 1e6;
int a[M];
int v[M], p[M], m;

void prime(int n) {
    memset(v, 0, sizeof(v));
    for(int i = 2; i <= n; ++i) {
        if(!v[i]) v[i] = i, p[m++] = i;
        for(int j = 1; j <= m; ++ j) {
            if(p[j] > v[i] || p[j] > n/i) break;
            v[i*p[j]] = p[j]; //i*p[j]的最小质因子
        }
    }
}

int main() {
    prime(M-1);
    for(int i = 1; i*i <= M; ++i) {
        for(int j = 0; j < m; ++ j) {
            int id = p[j] + i*i*2;
            if(id < M) a[id] = 1; 
        }
    }
    for(int i = 1; i < M; i+=2) {
        if(!a[i] && v[i] != i) {
            std::cout << i << std::endl;
        }
    }

    std::cout << "finished" << std::endl;
    int amo; std::cin >> amo;
}