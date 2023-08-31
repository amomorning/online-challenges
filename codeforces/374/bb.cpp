#include <bits/stdc++.h>
const int M = 1e5+10;

char s[M];

int main() {
	scanf("%s", s);
	int i = 1;
	int cnt;
	long long ans = 1;
	while(s[i]) {
		if(s[i]+s[i-1]-'0'-'0' == 9) {
			cnt = 2;
			i ++;
			while(s[i]+s[i-1]-'0'-'0' == 9) {
				i ++;
				cnt ++;
			}
			if(cnt&1) ans*=(cnt+1)/2;
		}else i ++;
	}
	printf("%lld\n", ans);
}
