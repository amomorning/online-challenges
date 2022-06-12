#include <bits/stdc++.h>
const int M = 5e3 +10;
int n;
char s[M];
int dp[M][M];

bool check(int i, int j) {
	if(i > j) return false;
	if(s[i] == '(' && s[j] == ')') return true;
	if(s[i] == '(' && s[j] == '?') return true;
	if(s[i] == '?' && s[j] == ')') return true;
	if(s[i] == '?' && s[j] == '?') return true;
	return false;
}

int main() {
	scanf("%s", s);
	n = strlen(s);
	for(int i = 0; i < n; i ++) dp[i][i] = 1;
	for(int i = 0; i < n; i ++) {
		for(int j = n-1; j > 0; j --) {
			if(check(i, j) && !dp[i+1][j-1]) {
				dp[i][j] = dp[i+1][j-1] + 1;
			}
		}
	}
	for(int i = 0; i < n; i ++) {
		for(int j = 0; j < n; j ++) {
			printf("%d ", dp[i][j]);
		}
		puts("");
	}
}
