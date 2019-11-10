#include <bits/stdc++.h>
const int M = 2e5+10;
int a[M], c[M], b[M];

int main() {
	int n, m; scanf("%d%d", &n, &m);
	for(int i = 0; i < n; ++ i) {
		scanf("%d", &a[i]);
		b[i] = a[i];
	}
	std::sort(b, b+n);
	for(int i = 0; i < m; ++ i) {
		int x, y; scanf("%d%d", &x, &y);
		x --, y --;
		if(a[x] > a[y]) c[x] --;
		if(a[x] < a[y]) c[y] --;
	}
	for(int i = 0; i < n; ++ i) {
		int pos = std::lower_bound(b,b+n,a[i]) - b;
		printf("%d ", pos + c[i]); 
	}
}
