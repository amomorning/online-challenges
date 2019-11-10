#include <bits/stdc++.h>
const int N = 1e5+10;

int a[N];

int main() {
	int n; scanf("%d", &n);
	for(int i = 0; i < n; ++ i) {
		scanf("%d", &a[i]);
	}
	std::sort(a, a+n);
	int m; scanf("%d", &m);
	for(int i = 0; i < m; ++ i) {
		int x;
		scanf("%d", &x);
		int p = std::lower_bound(a, a+n, x)-a;
		if(p == n) puts("Dr. Samer cannot take any offer :(.");
		else printf("%d\n", a[p]);
	}
}
