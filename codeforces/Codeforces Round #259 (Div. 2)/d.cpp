#include <bits/stdc++.h>
int a[110], b[110];
int n;

bool check() {
	for(int i = 0; i < n; i ++) {
		if(b[i] < 0) return false;
		for(int j = 0; j < n; j ++) if(i!=j) {
			if(std::__gcd(b[i], b[j]) != 1) return false;
		}
	}
	return true;
}

void dfs(int deep) {
	if(deep == n) {
		for(int i = 0; i < n; i ++) {
			printf("%d ", b[i]);
		}
		exit(0);
	}
	for(int i = 0; i <= 30; i ++) {
		b[deep] = a[deep] + i;
		if(check()) dfs(deep+1);
		if(deep) b[deep] = a[deep] - i;
		if(check()) dfs(deep+1);
		b[deep] = 1;
	}
}

int main() {
	scanf("%d", &n);
	for(int i = 0; i < n; i ++) {
		scanf("%d", &a[i]);
		b[i] = 1;
	}
	// std::sort(a, a+n);
	dfs(0);
}
