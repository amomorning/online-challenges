#include <bits/stdc++.h>
const int M = 1e6;

int a[M];

int main() {
    for(int i = 2; i < M; ++ i) {
        int tmp = i;
        for(int j = 2; j*j <= i; ++ j) {
            if(tmp%j == 0) {
                while(tmp%j == 0) tmp /= j;
                a[i] ++;
            }
        }
        if(tmp > 1) a[i]++;
    }
    for(int i = 2; i < M; ++ i) {
        bool flag = true;
        // printf("%d - %d\n",i, a[i]);
        for(int j = 0 ; j < 4; ++ j) if(a[i+j] != 4) flag = false;
        if(a[i+4] == 4) flag = false;
        if(flag) printf("%d\n", i);
    }

    std::cout << "finished" << std::endl;
    int amo; std::cin >> amo;
}