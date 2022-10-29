#include <bits/stdc++.h>

int main() {
    int cas;
    std::cin >> cas;
    while (cas --) {
        int n;
        std::cin >> n;
        std::vector<std::pair<int, int>> v;
        for(int i = 0; i < n; ++ i) {
            int a, b;
            std::cin >> a >> b;
            if(a > b) {
                v.emplace_back(std::make_pair(a, b));
            } else {
                v.emplace_back(std::make_pair(b, a));
            }
        }
        std::sort(v.begin(), v.end());
        long long ans = 0;
        int last = 0x3f3f3f3f;
        for(int i = 0; i < v.size(); ++ i) {
            if(ans > 0) {
                ans -= 1ll* std::min(last, v[i].first) * 2;
            }
            ans += 1ll*(v[i].first + v[i].second) * 2;
            last = v[i].first;
        }
        std::cout << ans << std::endl;
    }
}
