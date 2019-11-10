#include <bits/stdc++.h>
const int M = 5000;
int a[M];

bool check(int d) {
    for(int i = 0; i < M; ++ i) {
        for(int j = i+1; j < M; ++ j) {
            if(a[j] - a[i] > d) break;
            int pos = std::lower_bound(a, a+M, a[i]+a[j]) - a;
            int pos2 = std::lower_bound(a, a+M, a[j]-a[i]) -a;
            if(a[pos] == a[i] + a[j] && a[pos2] == a[j]-a[i]) return true; 
        }
    }
    return false;
}

int main() {
    for(int i = 0; i < M; ++ i) a[i] = (i+1)*(3*i+2)/2;
    
    int l = 0, r = 1e9;
    while(l < r) {
        int mid = (l+r) >> 1;
        if(check(mid)) {
            r = mid;
            std::cout << "check now " << mid << std::endl;
        }
        else l = mid+1;
    }
    printf("%d\n", r);
    int amo; std::cin>>amo;
}