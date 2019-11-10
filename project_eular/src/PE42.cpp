#include <bits/stdc++.h>

int a[5555];

int main() {
    freopen("data/p042_words.txt", "r", stdin);
    freopen("data/out.txt", "w", stdout);
    std::string str;
    std::cin >> str;
    for(int i = 1; i <= 100; ++i) {
        a[i*(i+1)/2] = 1;
    }

    int cnt = 0;
    int ans = 0;
    for(int i = 0; i < str.size(); ++ i) {
        if(str[i] == '\"') {
            if(a[cnt]) ans ++;
            cnt = 0;
        } 
        if(std::isalpha(str[i])) {
            cnt += str[i]-'A'+1;
        }
    }
    std::cout << ans << std::endl;
    // ans = 162
}
