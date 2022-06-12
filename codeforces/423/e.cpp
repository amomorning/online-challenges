#include <bits/stdc++.h>
#define lson o<<1,l,mid
#define rson o<<1|1,mid+1,r
using namespace std;
const int M = 1e5+10;


struct Segtree{
    int T[M<<2];
    void up(int o) {
        T[o] = T[o<<1] + T[o<<1|1];
    }
    void update(int o, int l, int r, int i, int x) {
        if(l == r) {
            T[o] += x;
            return;
        }
        int mid = l+r>>1;
        if(i<=mid) update(lson, i, x);
        else update(rson, i, x);
        up(o);
    }
    int ask(int o, int l, int r, int pl, int pr) {
        if(pl <= l && r <= pr) {
            return T[o];
        }
        int mid = l+r>>1;
        int ret = 0;
        if(pl <= mid) ret += ask(lson, pl, pr);
        if(pr > mid) ret += ask(rson, pl, pr);
        return ret;
    }
};

vector<Segtree> v[4][10];
char s[M]; char a[11];
int mp[128];

int main() {
    mp['A'] = 0; mp['T'] = 1; mp['G'] = 2; mp['C'] = 3;
    for(int i = 0; i < 4; i ++) 
        for(int j = 1; j <= 10; j ++) 
            v[i][j].resize(j);
    scanf("%s", s);
    int n = strlen(s)-1;
    for(int i = 0; s[i]; i ++) {
        for(int j = 1; j <= 10; j ++) {
            v[mp[s[i]]][j][i%j].update(1, 0, n, i, 1);
        }
    }
    int q; scanf("%d", &q);
    while(q--) {
        int op; scanf("%d", &op);
        if(op == 1) {
            int x;
            scanf("%d%s", &x, a); 
            x --;
            for(int i = 1; i <= 10; i ++) {
                v[mp[s[x]]][i][x%i].update(1, 0, n, x, -1);
            }
            s[x] = a[0];
            for(int i = 1; i <= 10; i ++) {
                v[mp[s[x]]][i][x%i].update(1, 0, n, x, 1);
            }
        } else {
            int l, r; scanf("%d%d%s", &l, &r, a);
            l --, r --;
            int len = strlen(a);
            int ans = 0;
            for(int i = 0; i < len; i ++) {
                int k = (l+i) % len;
                ans += v[mp[a[i]]][len][k].ask(1, 0, n, l, r);
            }
            printf("%d\n", ans);
        }
    }
}
