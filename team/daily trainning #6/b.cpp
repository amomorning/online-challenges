#include <bits/stdc++.h>

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n, a;
		scanf("%d%d", &n, &a);
		int m = 2*a-1;
		if(n <= m) {
			printf("%d\n", n);
			continue;
		}
		int i = 1;
		n -= m;
		int ans = m;
		while(n && a > i) {	
			if(n > (i+2)*(a-i)) {
				ans += a-i;
				n -= (i+2)*(a-i);
			} else ans += n/(i+2);
			i ++;
		}
		printf("%d\n", ans);
	}
}
