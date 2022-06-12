#include <bits/stdc++.h>
const int N =1e4+10;

char s[N];
int sum[30][N];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		memset(sum, 0, sizeof(sum));
		int n, m; scanf("%d%d", &n, &m);
		scanf("%s", s+1);
		for(int i = 1; i <= n; ++ i) {
			sum[s[i]-'a'][i] ++;
		}
		for(int i = 0; i < 26; ++ i) {
			for(int j = 1; j <= n; ++ j) {
				sum[i][j] += sum[i][j-1];
			}
		}
		while(m --) {
			int l, r;
			char ch[2];
			scanf("%d%d%s", &l, &r, ch);
			r --, l --;
			int cnt = r/n - l/n - 1; 
			l = l%n+1;
			r = r%n+1;
			int ans = 0;
			int c = ch[0]-'a';
			if(cnt == -1) {
				ans = sum[c][r] - sum[c][l-1];
			} else {
				ans += sum[c][n]*cnt;
				ans += sum[c][r];
				ans += sum[c][n] - sum[c][l-1];
			}
			printf("%d\n", ans);
		}
	}
}
