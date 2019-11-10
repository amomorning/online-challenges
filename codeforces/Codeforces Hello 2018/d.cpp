#include <bits/stdc++.h>
const int M = 2e5+10;

int a[M], t[M], idx[M];
int n, T;

bool c(int x) {
    int cnt = 0, sum = 0;
    for(int i = 0; i < n; ++ i) {
        int id = idx[i];
        if(a[id] < x) continue;
        sum += t[id];
        if(sum > T) break;
        cnt ++;
    }
    return cnt < x;
}

int main() {
    scanf("%d%d", &n, &T);
    for(int i = 0; i < n; ++ i) {
        scanf("%d%d", &a[i], &t[i]);
        idx[i] = i;
    }
    std::sort(idx, idx+n, [&](int x, int y) {
            return t[x] < t[y];
            });
    int l = 0, r = M;
    while(l < r) {
        int mid = (l+r+1) >> 1;
        if(c(mid)) r = mid-1;
        else l = mid;
    }
    printf("%d\n%d\n", l, l);
    std::vector<int> ans;
    for(int i = 0; i < n; i ++) {
        if(ans.size() == l) break;
        int id = idx[i];
        if(a[id] >= l) ans.push_back(id+1);
    }
    for(int x:ans) printf("%d ", x);
}
