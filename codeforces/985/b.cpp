#include <bits/stdc++.h>

char mp[2010][2010];
int cnt[2010];

int main() {
	int n, m; scanf("%d%d", &n, &m);
	for(int i = 0; i < n; ++ i) {
		scanf("%s", mp[i]);
		for(int j = 0; j < m; ++ j) {
			if(mp[i][j] == '1') cnt[j] ++;
		}
	}
	for(int i = 0; i < n; ++ i) {
		bool flag = true;
		for(int j = 0; j < m; ++ j) {
			if(mp[i][j] == '1' && cnt[j] == 1) {
				flag = false;
			}
		}
		if(flag) return puts("YES"), 0;
	}
	puts("NO");
}
