#include <bits/stdc++.h>
using namespace std;
const int M = 2e6+10;
set<int> st;
char t[M], s[M];

int main() {
    for(int i = 0; i < M; i ++) {
        st.insert(i);
    }
    int n; scanf("%d", &n);
    int m = 0;
    while(n --) {
        int k;
        scanf("%s%d", s, &k);
        int len = strlen(s);
        for(int i = 0; i < k; i ++) {
            int x; scanf("%d", &x); x--; 
            auto it = st.lower_bound(x);
            while(*it < x + len) {
                m = max(m, *it);
                t[*it] = s[*it-x];
                st.erase(*it);
                it = st.lower_bound(x);
            }
        }
    }
    for(int i = 0; i <= m; i ++) {
        printf("%c", t[i]=='\0'?'a':t[i]);
    }
    puts("");
}
