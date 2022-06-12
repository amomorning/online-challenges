#include <bits/stdc++.h>
using namespace std;
const int M = 4e6+10;

vector<int> v;
char s[M], t[M];
int f[M];

int main() {
    memset(t, '\0', sizeof(t));
    int n; scanf("%d", &n);
    int mx = 0;
    while(n --) {
        int k; scanf("%s%d", s, &k);
        int len = strlen(s);
        for(int i = 0; i < k; i ++) {
            v.clear();
            int x; scanf("%d", &x);
            if(f[x] == 0 || f[x+len-1] - f[x-1]+1 < len) v.push_back(x);
            for(int i = 0; i < v.size(); i ++) {
                int pos = v[i];
                for(int j = 0; s[j]; j ++) {
                    f[pos] = f[pos-1] + 1;
                    t[pos ++] = s[j]; 
                    mx = max(mx, pos);
                }
            }
        }
    }
    for(int i = 1; i < mx; i ++) {
        if(t[i] == '\0') t[i] = 'a';
    }
    printf("%s\n", t+1);
    return 0;
}
