#include <bits/stdc++.h>
const int MAX = 2e6+10;
int a[MAX];

int main() {
    int n; scanf("%d", &n);
    for(int i = 0; i < n; ++ i) {
        scanf("%d", &a[i]);
    }
    std::sort(a, a + n);

    bool flag = false;
    for(int i = 1; i < n; ++ i) {
        // printf("%d ", a[i]);
        if(a[i] == a[i - 1]) {
            flag = true;
            break;
        }
    }

    if(flag) puts("NO");
    else puts("YES");

    int amo; std::cin >> amo;
}
