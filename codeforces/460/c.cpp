#include <bits/stdc++.h>
const int M = 2e3+10;

int a[M][M], b[M][M];
char s[M][M];

int main() {
	int n, m, k;
	scanf("%d%d%d", &n, &m, &k);
	k --;
	int ans = 0;
	for(int i = 0; i < n; i ++) {
		scanf("%s", s[i]);
		for(int j = 1; j < m; j ++) {
			if(s[i][j] == s[i][j-1] && s[i][j] == '.') {
				a[i][j] = a[i][j-1]+1;
			}	
		}
	}
	for(int j = 0; j < m; j ++) {
		for(int i = 1; i < n; i ++) {
			if(s[i][j] == s[i-1][j] && s[i][j] == '.') {
				b[i][j] = b[i-1][j]+1;
			}
		}
	}
	for(int i = 0; i < n; i ++) {
		for(int j = 0; j < m; j ++) {
			if(a[i][j] >= k) ans ++;
			if(b[i][j] >= k) ans ++;
		}
	}
	printf("%d\n", k?ans:ans/2);
}
