#include <bits/stdc++.h>
const int M = 1e5+10;
int a[M];

int main() {
	int n;
	scanf("%d", &n);
	int mx = -1;
	for(int i = 0; i < n; i ++) {
		int x; scanf("%d", &x);
		a[x] ++;
	}
	bool flag = true;
	for(int i = M; i > 0; -- i) {
		if(a[i]&1) flag = false;
	}
	if(flag) puts("Agasa");
	else puts("Conan");
}
