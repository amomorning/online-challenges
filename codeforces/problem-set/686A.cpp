#include <bits/stdc++.h>

int main() {
    int n;
    long long m; scanf("%d%I64d", &n, &m);

    int cnt = 0;
    for(int i = 0; i < n; ++ i) {
        char op[2]; 
        int num; 
        scanf("%s%d", op, &num);
        if(op[0] == '+') {
            m += num;
        } else {
            if(m >= num) m-=num;
            else cnt ++;
        }
    }
    printf("%I64d %d\n", m, cnt);
    int amo; std::cin >> amo;
}
