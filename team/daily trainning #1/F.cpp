#include <bits/stdc++.h>
using namespace std;

vector<pair<int,int> > v;
int num[30];
char s[110];
int main() {
    scanf("%s", s);
    for(int i = 0; s[i]; i ++) {
        num[s[i]-'a'] ++;
    }
    for(int i = 0; i < 26; i ++) {
        if(num[i]) {
            v.emplace_back(num[i], i);
        }
    }
    sort(v.begin(), v.end());
    int ans = 0;
    if(v.size() > 2) {
        for(int i = 0; i < v.size()-2; i ++) {
            ans += v[i].first;   
        }
    }
    printf("%d\n", ans);
}
