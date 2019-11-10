#include <bits/stdc++.h>
typedef long long ll;

std::priority_queue<int> pq;

int main() {
    ll n;
    int k; scanf("%lld%d", &n, &k);
    int cnt = 0;
    while(n) {
        if(n%2) pq.push(cnt);
        n /= 2;
        cnt ++;
    }
    if(pq.size() > k) {
        return puts("No"), 0;    
    }
    k -= pq.size();
    while(k) {
        int tmp = pq.top(); pq.pop();
        tmp --;
        pq.push(tmp);
        pq.push(tmp);
        k --;
    }
    puts("Yes");
    while(!pq.empty()) {
        printf("%d ", pq.top());
        pq.pop();
    }
}
