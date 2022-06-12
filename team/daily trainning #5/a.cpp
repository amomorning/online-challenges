#include <bits/stdc++.h>
using namespace std;

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int a, b; scanf("%d%d", &a, &b);
		printf("%d\n", (int)floor(1.0*a/(1.0+1.0*b/100)));
	}
}
