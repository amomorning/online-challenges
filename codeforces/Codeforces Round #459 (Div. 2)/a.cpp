#include <bits/stdc++.h>
int a[1100];
int f[55];

int main() {
	int n;
	scanf("%d", &n);
	f[1] = 1;
	f[2] = 1;
	for(int i = 3; i < 17; i ++) {
		f[i] = f[i-1] + f[i-2];
		a[f[i]] = 1;
		// printf("%d %d\n",i, f[i]);
	}
	a[1] = 1, a[2] = 1;
	for(int i = 1; i <= n; i ++) {
		if(a[i]) printf("O");
		else printf("o");
	}
}
