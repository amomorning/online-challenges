#include <bits/stdc++.h>

int main() {
	int a, b, c;
	scanf("%d%d%d", &a, &b, &c);
	if(a > b) std::swap(a, b);
	if(a+c >= b ) c -= (b-a), a = b;
	else a += c, c = 0;
	printf("%d\n", (a+c/2)*2);
}
