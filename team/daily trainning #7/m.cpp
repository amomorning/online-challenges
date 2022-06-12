#include <bits/stdc++.h>

bool check(int x) {
	while(x) {
		int tmp = x%10;
		if(tmp == 0) return false;
		x /= 10;
	}
	return true;
}

int main() {
	int n; scanf("%d", &n);
	n++;
	for(int i = n; ; ++ i) {
		if(check(i)) {
			printf("%d\n", i);
			break;
		}
	}
}
