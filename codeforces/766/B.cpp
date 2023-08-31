#include <bits/stdc++.h>
using namespace std;
const int M = 1e5+10;
int a[M];

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i ++) {
        scanf("%d", &a[i]);
    }
    sort(a, a+n);
    reverse(a, a+n);
    bool flag = false;
    for(int i = 0; i < n-2; i ++) {
        if(a[i+1] + a[i+2] > a[i]) {
            flag = true;
            break;
        }
    }
    if(flag) puts("YES");
    else puts("NO");
}
