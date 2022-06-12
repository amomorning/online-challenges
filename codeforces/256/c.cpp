#include <bits/stdc++.h>
const int M = 5e3+10;
int a[M];

int dfs(int l, int r, int base) {
	if(l >= r) return 0;
	int mni = l; 
	for(int i = l; i < r; i ++) if(a[mni] > a[i]) {
		mni = i;
	}
	int cnt = a[mni]-base;
	int ls = l;
	for(int i = l; i < r; i ++) {
		if(a[i] == a[mni]) {
			cnt += dfs(ls, i, a[mni]);
			ls = i+1;
		}
	}
	cnt += dfs(ls, r, a[mni]);
	return std::min(r-l, cnt);
}

int main() {
	int n; scanf("%d", &n);
	for(int i = 0; i < n; i ++) scanf("%d", &a[i]);
	printf("%d\n", dfs(0, n, 0));
}
