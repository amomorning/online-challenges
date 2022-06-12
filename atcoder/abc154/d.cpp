#include <bits/stdc++.h>
const int MAX = 2e5+10;

int a[MAX], s[MAX];

int main() {
    int n, k;
    scanf("%d%d", &n, &k);

    for(int i = 0; i < n; ++ i) {
        scanf("%d", &a[i]);
        if(i) s[i] = s[i-1] + a[i];
        else s[i] = a[i];
    }

    int mx = s[k-1];
    for(int i = k; i < n; ++ i) {
        if(s[i] - s[i-k] > mx) mx = s[i] - s[i-k];
    }

    printf("%.12f\n", 0.5*(mx+k));
    int amo; std::cin >> amo; 
}
