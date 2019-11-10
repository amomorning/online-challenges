#include <bits/stdc++.h>

int main() {
	int t;  scanf("%d", &t);
	while(t --) {
		int a, b, c, d;
		scanf("%d%d%d%d", &a, &b, &c, &d);
		double x = log(a)*b;
		double y = log(c)*d;
		printf("%c\n", "<>"[x>y]);
	}
}
