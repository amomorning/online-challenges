#include <bits/stdc++.h>

std::vector<int> vv;
int vis[11111];

bool isprime(int x) {
    for(int i = 2; i*i <= x; ++ i) {
        if(x%i == 0) return false;
    }
    return true;
}

bool check(int x, int dig) {
    while(x) {
        if(dig == x%10) return false;
        x /= 10;
    }
    return true;
}

void dfs(int cur, int dep) {
    if(dep == 4) {
        if(isprime(cur)) {
            vv.push_back(cur);
        }  
        return;
    }
    for(int i = 0; i <= 9; ++ i) {
        dfs(cur*10+i, dep+1);
    }
}

bool same(int a, int b) {
    int aa[4], bb[4];
    for(int i = 0; i < 4; ++ i) {
        aa[i] = a%10;
        bb[i] = b%10;
        a /= 10;
        b /= 10;
    }
    std::sort(aa, aa+4);
    std::sort(bb, bb+4);
    for(int i = 0; i < 4; ++ i) {
        if(aa[i] != bb[i]) return false;
    }
    return true;
}

int main() {
    for(int i = 1; i <= 9; ++ i) {
        dfs(i, 1);
    }
    int n = vv.size();

    for(int i = 0; i < n; ++ i) {
        if(vis[vv[i]]) continue;
        vis[vv[i]] = 1;
        std::vector<int> tmp;
        tmp.push_back(vv[i]);
        for(int j = i+1; j < n; ++ j) {
            if(same(vv[i], vv[j])) {
                vis[vv[j]] = 1;
                tmp.push_back(vv[j]);
            }
        }
        if(tmp.size() < 3) continue;

        for(int x = 0; x < tmp.size(); ++ x) {
            for(int y = x+1; y < tmp.size(); ++ y) {
                for(int z = y+1; z < tmp.size(); ++ z) {
                    if(tmp[x] + tmp[z] == tmp[y] + tmp[y]) printf("%d%d%d\n", tmp[x], tmp[y], tmp[z]);
                }
            }
        }

    }
    int amo; std::cin>>amo;
}