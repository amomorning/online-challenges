#include <bits/stdc++.h>
const int M = 1e5+10;
int a[M];

int main() {
	int n, k; scanf("%d%d", &n, &k);
	for(int i = 0; i < n; ++ i) {
		int t; scanf("%d", &t);
		a[i%k] += t;
	}
	int m = 0;
	for(int i = 0; i < k; ++ i) {
		if(a[m] > a[i]) m = i;
	}
	printf("%d\n", m+1);
}
