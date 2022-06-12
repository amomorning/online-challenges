#include <bits/stdc++.h>
const int M = 5e3+10;
char s[M];

int main() {
	scanf("%s", s);
	int ans = 0;
	for(int i = 0; s[i]; i ++) {

		int l = 0, r = 0;
		if(s[i] == ')') continue;
		for(int j = i; s[j]; j ++) {
			if(s[j] == '(') {
				l ++;
			}else if(s[j] == ')') {
				l --;
			}else {
				r ++;
				l --;
			}
			if(l < 0 && r > 0) r --, l += 2;
			if(l == 0) ans ++;
			if(l < 0) break;
		}
	}
	printf("%d\n", ans);
}
