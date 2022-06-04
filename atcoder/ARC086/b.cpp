#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    scanf("%d%d", &a, &b);
    int t = b;
    int tmp = 1;
    while(t) t/=10, tmp*=10;
    t = a*tmp+b;
    int c = sqrt(t);
    if(c*c == t) puts("Yes");
    else puts("No");
}
