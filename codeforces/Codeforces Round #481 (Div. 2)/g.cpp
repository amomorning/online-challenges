#include <bits/stdc++.h>
int sc[110];
int main() {
	int n, m; scanf("%d%d", &n, &m);
	bool f = 1;
	for(int i = 0; i < m; ++ i) {
		int s, d, c; scanf("%d%d%d", &s, &d, &c);
		sc[d] = m+1;
		int tot = 0;
		for(int j = s; j < d; ++ j) {
			if(sc[j] == 0) {
				sc[j] = i+1;
				tot ++;
			}
			if(tot == c) break;
		}
		if(tot < c) f = 0;
	}
	if(f) {
		for(int i = 1; i <= n; ++ i) {
			printf("%d ", sc[i]);
		}
	} else puts("-1");
}
