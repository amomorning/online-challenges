#include <bits/stdc++.h>

int n;
long long k;

int c(int m) {
	return (n-1+n-m)*m/2 >= k;
}

int main() {
	scanf("%d", &n);
	k = (1ll*n*(n-1)/2+1)/2;
	int l = 1, r = n-1;
	while(l < r) {
		int m = (l+r)>>1;
		if(c(m)) r = m;
		else l = m+1;
	}
	printf("%d\n", r);
}
