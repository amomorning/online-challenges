#include <bits/stdc++.h>

int main() {
    int q; scanf("%d", &q);
    while(q --) {
        long long a, b, c;
        scanf("%I64d%I64d%I64d", &a, &b, &c);
        printf("%I64d\n", (a+b+c) >> 1);
    }
}
