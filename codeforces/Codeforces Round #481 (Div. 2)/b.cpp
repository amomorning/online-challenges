#include <bits/stdc++.h>
char s[110];

int main() {
	int n; scanf("%d%s", &n, s);
	int cnt = 0, ans = 0;
	for(int i = 0; i < n; ++ i) {
		if(s[i] == 'x') {
			cnt ++;
		}
		else {
			if(cnt >= 3) ans += cnt-2;
			cnt = 0;
		}
	}
	if(cnt >= 3) ans += cnt-2;
	printf("%d\n", ans);
}
