#include <bits/stdc++.h>
int cnt[30];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d", &n);
		memset(cnt, 0, sizeof(cnt));
		for(int i = 0; i < n; ++ i) {
			char s[55];
			scanf("%s", s);
			cnt[s[0] - 'a'] ++;
		}
		int ans = std::min(cnt['b'-'a']/2, std::min(cnt['k'-'a'], cnt['l'-'a']));
		printf("%d\n", ans);
	}
}
