#include <bits/stdc++.h>

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n, x, y;
		scanf("%d%d%d", &n, &x, &y);
		int d = 0x3f3f3f3f, m = -1, idx;
		for(int i = 0; i < n; ++ i) {
			int a, b; scanf("%d%d", &a, &b);
			if(a > x || b < y) continue;
			if(a < d) {
				d = a;
				m = b;
				idx = i;
			} 
			if( a == d && b > m) {
				m = b;
				idx = i;
			}
		}
		if(m == -1) puts("-1");
		else printf("%d\n", idx+1);
	}
}
