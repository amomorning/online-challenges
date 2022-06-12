#include <bits/stdc++.h>

int main() {
	int a = 0, b = 0;
	for(int i = 0; i < 3; i ++) {
		int x;
		scanf("%d", &x);
		a += x;
	}
	for(int i = 0; i < 3; i ++) {
		int x;
		scanf("%d", &x);
		b += x;
	}
	int n; scanf("%d", &n);
	if((a+4)/5 + (b+9)/10 > n) puts("NO");
	else puts("YES");
}
