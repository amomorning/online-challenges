#include <bits/stdc++.h>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;
    if(a != b) printf("%d\n", max(a.length(), b.length()));
    else puts("-1");
    return 0; 
}
