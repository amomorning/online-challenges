#include <bits/stdc++.h>
std::string s, t, u;
int a, b;
int main() {
    std::cin >> s >> t;
    std::cin >> a >> b;
    std::cin >> u;

    if(s == u) a --;
    if(u == t) b --;

    std::cout << a << " " << b << std::endl; 

    int amo; std::cin >> amo;
}
