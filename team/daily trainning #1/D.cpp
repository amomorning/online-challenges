#include <bits/stdc++.h>
using namespace std;

struct name{
    string x, y;
}a[110];

bool cmp(name a, name b) {
    if(b.y == a.y) return a.x < b.x;
    return a.y < b.y;
}

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i ++) {
        cin >> a[i].x >> a[i].y;
    }
    sort(a, a+n, cmp);
    for(int i = 0; i < n; i ++) {
        cout << a[i].x << " " << a[i].y << endl;
    }
}
