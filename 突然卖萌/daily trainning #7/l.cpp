#include <bits/stdc++.h>

int n;

bool check(int a, int b) {
	if(n%(a+b) == 0) return true;
	if((n+b)%(a+b) == 0) return true;
	return false;
}

int main() {
	scanf("%d", &n);
	printf("%d:\n", n);
	for(int i = 2; i <= (n+1)/2; ++ i) {
		if(check(i, i-1)) {
			printf("%d,%d\n", i, i-1);
		}
		if(check(i, i)) {
			printf("%d,%d\n", i, i);
		}
	}
}
