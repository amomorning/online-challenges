#include <bits/stdc++.h>

char a[55][55];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n, m; scanf("%d%d", &n, &m);
		for(int i = 0; i < n; ++ i) scanf("%s",a[i]);
		int cz = 0;
		for(int i = 0; i < m; ++ i) {
			if(a[0][i] == '0') cz ++;
			if(a[n-1][i] == '0') cz ++;
		}
		for(int i = 1; i < n-1; ++ i) {
			if(a[i][0] == '0') cz ++;
			if(a[i][m-1] == '0') cz ++;
		}
		int co = 0;
		for(int i = 1; i < n-1; ++ i) {
			for(int j = 1; j < m-1; ++ j) {
				if(a[i][j] == '1') co ++;
			}
		}
		if(co < cz) printf("-1\n");
		else printf("%d\n", cz);
	}
}
