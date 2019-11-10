#include <bits/stdc++.h>
using namespace std;
vector<int> v;
vector<pair<int,int> > edge;
int main() {
    int n, k;
    scanf("%d%d", &n, &k);
    int t = (n-k-1)/k, tm = (n-k-1)%k;
    //printf("%d %d\n", t, tm);
    int num = 2*t + 2;
    if(tm >= 1) num ++;
    if(tm > 1) num ++;
    if(t) {
        for(int i = 0; i < k; i ++) {
            edge.emplace_back(1, 1+i+1);
            v.push_back(1+i+1);
        }
    } else if(tm) {
        v.push_back(1);
        for(int i = 0; i < tm; i ++) {
            edge.emplace_back(1, 1+i+1);
            v.push_back(i+1+1);
        }
        tm = 0;
    }
    for(int i = 1; i < t; i ++) {
        for(int j = 0; j < v.size(); j ++) {
            edge.emplace_back(v[j], v[j]+k);
            v[j] += k;
        }
    }
    for(int i = 0; i < tm; i ++) {
        edge.emplace_back(v[i], v[i]+k);
        v[i] += k;
    }

    int now = 1;
    for(int i = 0; i < v.size(); i ++) {
        now = max(now, v[i]);
    }
    for(int i = 0; i < k; i ++) {
        if(i >= v.size()) {
            edge.emplace_back(1, ++now);
        } else edge.emplace_back(v[i], ++now);
    }
    printf("%d\n", num);
    for(int i = 0; i < edge.size(); i ++) {
        printf("%d %d\n", edge[i].first, edge[i].second);
    }
}
