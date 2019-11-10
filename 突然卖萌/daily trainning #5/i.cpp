#include <bits/stdc++.h>
char ch[255][22];
int a[11], b[11];
int mp[255][255];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n, s, e; scanf("%d%d%d", &n, &s, &e);
		for(int i = 0; i < n; ++ i) {
			scanf("%s", ch[i]);
		}
		memset(mp, 0x3f, sizeof(mp));
		for(int i = 0; i < n; ++ i) {
			for(int j = 0; j < i; ++ j) {
				std::fill(a, a+10, 0);
				std::fill(b, b+10, 0);
				for(int k = 0; k < 20; ++ k) {
					a[ch[i][k] - '0'] ++;
					b[ch[j][k] - '0'] ++;
				}
				int com = 0;
				for(int k = 0; k < 10; ++ k) {
					com += std::min(a[k], b[k]);
				}
				if(com == 17) {
					mp[i][j] = 1;
					mp[j][i] = 1;
				}
			}
		}
		for(int k = 0; k < n; ++ k) {
			for(int i = 0; i < n; ++ i) {
				for(int j = 0; j < n; ++ j) {
					mp[i][j] = std::min(mp[i][j], mp[i][k] + mp[k][j]);
				}
			}
		}
		s --, e --;
		if(mp[s][e] == 0x3f3f3f3f) puts("-1");
		else printf("%d\n", mp[s][e]);
	}
}
