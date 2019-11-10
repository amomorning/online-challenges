#include <bits/stdc++.h>
const int M = 1e5+10;

char s[M];
int tot, n, cnt;

void dfs(int u, int now) {
	if(u >= n) {
		if(now == tot) cnt ++;
		return;
	}
	if(s[u]-'0' + s[u-1]-'0' == 9) {
		dfs(u+2, now+1);
		if(u+1 < n && s[u] -'0' + s[u+1]-'0' == 9) 
			dfs(u+3, now+1);
	} else dfs(u+1, now);
}

int main() {
	scanf("%s", s);
	tot = 0;
	n = strlen(s);
	for(int i = 1; s[i]; ++ i) {
		if(s[i]-'0' + s[i-1] - '0' == 9) tot ++, i ++;
	}
	cnt = 0;
	dfs(1, 0);
	printf("%d\n", cnt);
}
