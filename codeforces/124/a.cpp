#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, r;
    scanf("%d%d%d", &a, &b, &r);
    r*=2;
    if(r > a || r > b) puts("Second");
    else puts("First");
    return 0;
}
