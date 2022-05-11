#include <bits/stdc++.h>
const int M = 100000;
long long tri[M], pen[M], hex[M];

int main() {
    for(int i = 0; i < M; ++ i) {
        tri[i] = 1ll*(i+1)*(i+2)/2;
        pen[i] = 1ll*(i+1)*(3*i+2)/2;
        hex[i] = 1ll*(i+1)*(2*i+1);
    }
    for(int i = 0; i < M; ++ i) {
        int t = std::lower_bound(tri, tri+M, hex[i]) - tri;
        int p = std::lower_bound(pen, pen+M, hex[i]) - pen;

        if(tri[t] == pen[p] && tri[t] == hex[i]) {
            std::cout << hex[i] << std::endl;
        }
    }

    int amo; std::cin >> amo;
}